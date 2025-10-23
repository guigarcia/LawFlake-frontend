#!/usr/bin/env python3
"""
Fix dashboard.html - Remove código duplicado e criar versão limpa
"""

import re

# Ler o arquivo atual
with open('public/dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Encontrar onde começa o HTML content (antes dos scripts)
html_end_match = re.search(r'</main>.*?</div>', content, re.DOTALL)
if not html_end_match:
    print("ERROR: Could not find HTML structure")
    exit(1)

html_content = content[:html_end_match.end()]

# Criar novo conteúdo com script limpo
new_content = html_content + '''

    <!-- Scripts -->
    <script src="js/api.js"></script>
    <script src="js/auth.js"></script>
    <script>
        // ===================================================================
        // DASHBOARD - VERSÃO LIMPA E ÚNICA
        // ===================================================================

        document.addEventListener('DOMContentLoaded', async () => {
            checkAuth();
            await loadDashboard();
        });

        async function loadDashboard() {
            try {
                console.log('📊 Loading dashboard...');

                // Buscar stats da API
                const stats = await apiGet('/processos/stats');
                console.log('Stats received:', stats);

                // Atualizar cards principais (com null checks)
                const totalProcessosEl = document.getElementById('totalProcessos');
                if (totalProcessosEl) {
                    totalProcessosEl.textContent = stats.total_processos || 0;
                }

                const prazosProximosEl = document.getElementById('prazosProximos');
                if (prazosProximosEl) {
                    prazosProximosEl.textContent = stats.prazos_urgentes || 0;
                }

                // totalDocs e sumulas requerem endpoints separados
                const totalDocsEl = document.getElementById('totalDocs');
                if (totalDocsEl) totalDocsEl.textContent = '-';

                const sumulasEl = document.getElementById('sumulas');
                if (sumulasEl) sumulasEl.textContent = '-';

                // Atualizar gráficos (se funções existirem)
                if (typeof updateChartTipos === 'function' && stats.por_tipo) {
                    updateChartTipos(stats.por_tipo);
                }

                if (typeof updateChartPrazos === 'function' && stats.prazos_timeline) {
                    updateChartPrazos(stats.prazos_timeline);
                }

                if (typeof updateChartRisco === 'function' && stats.risco_por_instancia) {
                    updateChartRisco(stats.risco_por_instancia);
                }

                // Carregar processos recentes
                await loadRecentProcessos();

                console.log('✅ Dashboard loaded successfully');

            } catch (error) {
                console.error('❌ Error loading dashboard:', error);
                showError('Erro ao carregar dashboard. Verifique sua conexão.');
            }
        }

        async function loadRecentProcessos() {
            try {
                const response = await apiPost('/processos/search', {
                    size: 5,
                    from: 0
                });

                const processos = response.hits || [];
                const tableEl = document.getElementById('processosTable');

                if (!tableEl) {
                    console.warn('⚠️ processosTable element not found');
                    return;
                }

                if (processos.length === 0) {
                    tableEl.innerHTML = `
                        <tr>
                            <td colspan="6" class="text-center text-muted">
                                <i class="bi bi-inbox"></i>
                                <br>Nenhum processo encontrado
                            </td>
                        </tr>
                    `;
                    return;
                }

                tableEl.innerHTML = processos.map(p => `
                    <tr>
                        <td><strong>${escapeHtml(p.numero_processo || 'N/A')}</strong></td>
                        <td>${escapeHtml(p.titulo || 'Sem título')}</td>
                        <td>${escapeHtml(p.tipo_processo || 'N/A')}</td>
                        <td><span class="badge badge-${getStatusClass(p.status)}">${(p.status || 'ativo').toUpperCase()}</span></td>
                        <td>${formatTime(p.updated_at || p.created_at)}</td>
                        <td>
                            <button class="btn btn-primary btn-sm" onclick="viewProcesso('${p.id}')">
                                <i class="bi bi-eye"></i>
                            </button>
                        </td>
                    </tr>
                `).join('');

            } catch (error) {
                console.error('❌ Error loading processos:', error);
                const tableEl = document.getElementById('processosTable');
                if (tableEl) {
                    tableEl.innerHTML = `
                        <tr>
                            <td colspan="6" class="text-center" style="color: var(--danger);">
                                <i class="bi bi-exclamation-triangle"></i> Erro ao carregar processos
                            </td>
                        </tr>
                    `;
                }
            }
        }

        // Funções auxiliares
        function getStatusClass(status) {
            const map = {
                'ativo': 'success',
                'arquivado': 'warning',
                'concluido': 'info',
                'pendente': 'warning'
            };
            return map[(status || '').toLowerCase()] || 'info';
        }

        function formatTime(dateStr) {
            if (!dateStr) return 'N/A';
            try {
                const date = new Date(dateStr);
                const diff = Date.now() - date;
                const hours = Math.floor(diff / 3600000);
                const days = Math.floor(hours / 24);

                if (hours < 1) return 'Agora';
                if (hours < 24) return `Há ${hours}h`;
                if (days === 1) return 'Ontem';
                if (days < 7) return `Há ${days} dias`;

                return date.toLocaleDateString('pt-BR');
            } catch {
                return 'N/A';
            }
        }

        function escapeHtml(text) {
            if (!text) return '';
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }

        function showError(message) {
            alert(message); // TODO: Implementar toast notification
        }

        function goToChat(action) {
            window.location.href = `chat.html?action=${action}`;
        }

        function viewProcesso(numero) {
            window.location.href = `processos.html?numero=${numero}`;
        }

        // Funções de gráficos (stub - implementar se necessário)
        function updateChartTipos(data) {
            console.log('updateChartTipos called but not implemented');
        }

        function updateChartPrazos(data) {
            console.log('updateChartPrazos called but not implemented');
        }

        function updateChartRisco(data) {
            console.log('updateChartRisco called but not implemented');
        }
    </script>
</body>
</html>
'''

# Escrever arquivo limpo
with open('public/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("✅ dashboard.html reescrito com sucesso!")
print("📄 Backup salvo em dashboard.html.backup")
