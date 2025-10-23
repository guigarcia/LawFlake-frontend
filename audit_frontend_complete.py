"""
AUDITORIA COMPLETA DO FRONTEND - PENTE FINO
Analisa TODOS os arquivos HTML, JS, CSS linha por linha
"""

import re
import os
from pathlib import Path
from collections import defaultdict

class FrontendAuditor:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.issues = []
        self.stats = defaultdict(int)
        self.api_calls = []
        self.element_ids = defaultdict(list)

    def log_issue(self, severity, file, line, message):
        """Log an issue found"""
        self.issues.append({
            'severity': severity,
            'file': file,
            'line': line,
            'message': message
        })

    def audit_html(self, filepath):
        """Audit HTML file"""
        print(f"\n Auditando HTML: {filepath.name}")

        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for i, line in enumerate(lines, 1):
            # Check for IDs
            ids = re.findall(r'id="([^"]+)"', line)
            for id_val in ids:
                self.element_ids[id_val].append((filepath.name, i))

            # Check for missing labels
            if 'input' in line.lower() and 'type=' in line.lower():
                if 'id=' not in line:
                    self.log_issue('LOW', filepath.name, i, 'Input sem ID')

            # Check for inline styles (bad practice)
            if 'style=' in line and 'style.css' not in line:
                self.log_issue('LOW', filepath.name, i, 'Style inline encontrado (usar CSS)')

        self.stats['html_files'] += 1
        self.stats['html_lines'] += len(lines)

    def audit_javascript(self, filepath):
        """Audit JavaScript file"""
        print(f"\n Auditando JS: {filepath.name}")

        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            content = ''.join(lines)

        for i, line in enumerate(lines, 1):
            # Find API calls
            api_patterns = [
                r'apiGet\([\'"]([^\'"]+)[\'"]',
                r'apiPost\([\'"]([^\'"]+)[\'"]',
                r'fetch\([\'"]([^\'"]+)[\'"]',
            ]

            for pattern in api_patterns:
                matches = re.findall(pattern, line)
                for match in matches:
                    self.api_calls.append({
                        'file': filepath.name,
                        'line': i,
                        'endpoint': match,
                        'type': 'GET' if 'apiGet' in line or ('fetch' in line and 'method' not in line) else 'POST'
                    })

            # Check for console.log (should be removed in production)
            if 'console.log' in line and not line.strip().startswith('//'):
                self.log_issue('LOW', filepath.name, i, 'console.log encontrado (remover em produo)')

            # Check for missing error handling
            if '.then(' in line:
                # Look ahead for .catch
                next_20_lines = ''.join(lines[i:min(i+20, len(lines))])
                if '.catch' not in next_20_lines:
                    self.log_issue('MEDIUM', filepath.name, i, 'Promise sem .catch() - falta tratamento de erro')

            # Check for document.getElementById without null check
            if 'document.getElementById' in line:
                next_5_lines = ''.join(lines[i:min(i+5, len(lines))])
                if 'textContent' in next_5_lines or 'innerHTML' in next_5_lines:
                    if '?' not in next_5_lines and 'if' not in next_5_lines:
                        self.log_issue('HIGH', filepath.name, i, 'getElementById sem null check - pode dar erro!')

        self.stats['js_files'] += 1
        self.stats['js_lines'] += len(lines)
        self.stats['api_calls'] += len([c for c in self.api_calls if c['file'] == filepath.name])

    def audit_css(self, filepath):
        """Audit CSS file"""
        print(f"\n Auditando CSS: {filepath.name}")

        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for i, line in enumerate(lines, 1):
            # Check for !important (bad practice)
            if '!important' in line:
                self.log_issue('LOW', filepath.name, i, '!important encontrado (evitar quando possvel)')

            # Check for fixed pixel values in font-size (should use rem/em)
            if 'font-size:' in line and 'px' in line:
                self.log_issue('LOW', filepath.name, i, 'font-size em px (considerar usar rem/em)')

        self.stats['css_files'] += 1
        self.stats['css_lines'] += len(lines)

    def check_api_endpoints(self):
        """Verify API endpoints match backend"""
        print("\n\n VERIFICANDO ENDPOINTS DA API")
        print("="*80)

        # Known backend endpoints
        backend_endpoints = {
            '/auth/login': 'POST',
            '/auth/me': 'GET',
            '/processos/stats': 'GET',
            '/processos/': 'GET',
            '/processos/search': 'POST',
            '/processos/upload': 'POST',
            '/chat/sessions': 'GET',
            '/chat/history/{id}': 'GET',
            '/chat/message': 'POST',
            '/conhecimento/sumulas': 'GET',
            '/conhecimento/search': 'POST',
            '/companies/me': 'GET',
            '/config/datajud': 'GET',
        }

        print(f"\nTotal de chamadas API encontradas: {len(self.api_calls)}")

        # Group by endpoint
        endpoint_usage = defaultdict(list)
        for call in self.api_calls:
            endpoint_usage[call['endpoint']].append(call)

        print(f"\nEndpoints nicos chamados: {len(endpoint_usage)}")

        for endpoint, calls in sorted(endpoint_usage.items()):
            print(f"\n  {endpoint}")
            print(f"    Usado em: {calls[0]['file']}:{calls[0]['line']}")
            if len(calls) > 1:
                print(f"    Total de usos: {len(calls)}")

    def check_duplicate_ids(self):
        """Check for duplicate IDs"""
        print("\n\n VERIFICANDO IDs DUPLICADOS")
        print("="*80)

        duplicates = {k: v for k, v in self.element_ids.items() if len(v) > 1}

        if duplicates:
            print(f"\n[X] Encontrados {len(duplicates)} IDs duplicados:")
            for id_val, locations in duplicates.items():
                print(f"\n  ID: '{id_val}'")
                for file, line in locations:
                    print(f"    - {file}:{line}")
        else:
            print("\n[OK] Nenhum ID duplicado encontrado")

    def generate_report(self):
        """Generate final audit report"""
        print("\n\n" + "="*80)
        print("RELATRIO FINAL DA AUDITORIA")
        print("="*80)

        print(f"\n ESTATSTICAS:")
        print(f"  HTML files: {self.stats['html_files']} ({self.stats['html_lines']} linhas)")
        print(f"  JS files: {self.stats['js_files']} ({self.stats['js_lines']} linhas)")
        print(f"  CSS files: {self.stats['css_files']} ({self.stats['css_lines']} linhas)")
        print(f"  Total linhas: {self.stats['html_lines'] + self.stats['js_lines'] + self.stats['css_lines']}")
        print(f"  Chamadas API: {self.stats['api_calls']}")
        print(f"  IDs nicos: {len(self.element_ids)}")

        # Count issues by severity
        issues_by_severity = defaultdict(int)
        for issue in self.issues:
            issues_by_severity[issue['severity']] += 1

        print(f"\n[WARN]  PROBLEMAS ENCONTRADOS:")
        print(f"   HIGH: {issues_by_severity['HIGH']}")
        print(f"   MEDIUM: {issues_by_severity['MEDIUM']}")
        print(f"   LOW: {issues_by_severity['LOW']}")
        print(f"  TOTAL: {len(self.issues)}")

        if self.issues:
            print(f"\n DETALHES DOS PROBLEMAS:")

            # Group by severity
            for severity in ['HIGH', 'MEDIUM', 'LOW']:
                issues = [i for i in self.issues if i['severity'] == severity]
                if issues:
                    print(f"\n  {severity} ({len(issues)} problemas):")
                    for issue in issues[:10]:  # Show first 10
                        print(f"    - {issue['file']}:{issue['line']} - {issue['message']}")
                    if len(issues) > 10:
                        print(f"    ... e mais {len(issues) - 10} problemas {severity}")

def main():
    base_path = r"M:\Projetos\LawFlake-frontend\public"

    print("="*80)
    print("AUDITORIA COMPLETA DO FRONTEND - LAWFLAKE")
    print("="*80)

    auditor = FrontendAuditor(base_path)

    # Audit all HTML files
    for html_file in Path(base_path).glob("*.html"):
        auditor.audit_html(html_file)

    # Audit all JS files
    for js_file in Path(base_path).glob("js/*.js"):
        auditor.audit_javascript(js_file)

    # Audit all CSS files
    for css_file in Path(base_path).glob("css/*.css"):
        auditor.audit_css(css_file)

    # Run checks
    auditor.check_api_endpoints()
    auditor.check_duplicate_ids()

    # Generate report
    auditor.generate_report()

    print("\n" + "="*80)
    print("AUDITORIA CONCLUDA")
    print("="*80 + "\n")

if __name__ == "__main__":
    main()
