# 🏛️ LawFlake Frontend - Prompt de Início

Cole este prompt na sessão do Claude dentro do repositório `M:\Projetos\LawFlake-frontend`:

---

## CONTEXTO

Você está trabalhando no **LawFlake Frontend** - interface profissional para advogados empresariais consultarem processos jurídicos via chat com IA.

### O que é o LawFlake?

Sistema que transforma PDFs de processos jurídicos em base de conhecimento consultável.

**Core feature**: **Quick Actions** - gatilhos rápidos (não chat livre):
1. 📄 Resumo Executivo
2. ⏰ Próximos Prazos
3. ⚠️ Análise de Risco
4. ⚖️ Precedentes Similares
5. 📊 Analytics
6. 📤 Exportar Relatório

### Público-Alvo: Advogados Empresariais

**Perfil**:
- 👔 Profissionais sérios (30-55 anos)
- 💼 Trabalham em escritórios ou departamentos jurídicos
- 💻 Usam desktop (não mobile-first)
- ⏱️ Precisam de eficiência (não têm tempo para chat livre)
- 🔍 Querem fontes citadas (confiança acima de tudo)

**Design Principles**:
- ✅ Seriedade e profissionalismo
- ✅ Máximo 2 cliques para qualquer ação
- ✅ Quick Actions como protagonistas (botões grandes)
- ✅ Sources SEMPRE visíveis
- ✅ Desktop-first (mobile é secundário)

---

## IDENTIDADE VISUAL

### Paleta de Cores

```css
/* Cores Principais */
--lawflake-primary: #1e3a5f;      /* Azul escuro profissional */
--lawflake-secondary: #2c5f8d;    /* Azul médio */
--lawflake-accent: #d4af37;       /* Dourado (elegância) */

/* Status e Feedback */
--lawflake-success: #2d5016;      /* Verde escuro */
--lawflake-warning: #8b6914;      /* Amarelo escuro */
--lawflake-danger: #8b1a1a;       /* Vermelho escuro */

/* Neutros */
--lawflake-bg: #f8f9fa;           /* Fundo claro */
--lawflake-text: #2c3e50;         /* Texto principal */
--lawflake-border: #dee2e6;       /* Bordas */
```

### Tipografia

```css
/* Fontes */
--lawflake-font-serif: 'Merriweather', 'Georgia', serif;  /* Títulos - elegância */
--lawflake-font-sans: 'Inter', 'Segoe UI', sans-serif;    /* Corpo - legibilidade */
--lawflake-font-mono: 'JetBrains Mono', 'Consolas', monospace;

/* Uso */
h1, h2, h3 { font-family: var(--lawflake-font-serif); }
body, p, span { font-family: var(--lawflake-font-sans); }
code, pre { font-family: var(--lawflake-font-mono); }
```

### Ícones

**Bootstrap Icons** (consistência com Bootstrap 5)
- 📂 Processo: `bi-folder-fill`
- ⚖️ Jurídico: `bi-scale`
- ⏰ Prazos: `bi-alarm`
- 🔴 Risco: `bi-exclamation-triangle-fill`

---

## STACK TÉCNICA

### Frontend
- **Vanilla JavaScript** (ES6+, sem frameworks)
- **Bootstrap 5.3** (UI components)
- **Bootstrap Icons** (ícones)
- **Chart.js** (gráficos)
- **Supabase JS** (auth)
- **DOMPurify** (XSS protection)

**Por que Vanilla JS?**
- Mais simples (sem build step)
- Mais rápido (sem bundle)
- Mais fácil manutenção

---

## CREDENCIAIS DISPONÍVEIS

### API Backend
```
URL: https://lawflake-production.up.railway.app
(ou http://localhost:8000 para dev local)
```

### Supabase (Auth)
```
URL: https://bydfdmmyzjdsfaomhwse.supabase.co
Anon Key: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ5ZGZkbW15empkc2Zhb21od3NlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjExMzA2MTIsImV4cCI6MjA3NjcwNjYxMn0.J1Ju2irp4qSPZWM4HwY8ZcIMo7kW6qchSGoa3XNShIE
```

### Deploy
```
Frontend Vercel: https://law-flake-frontend.vercel.app/
Backend Railway: lawflake-production.up.railway.app
```

---

## ESTRUTURA DE PASTAS

```
LawFlake-frontend/
├── public/
│   ├── index.html                # Redirect para login
│   ├── login.html                # Auth
│   ├── dashboard.html            # Dashboard principal
│   ├── processos.html            # Lista
│   ├── processo-detalhe.html     # Detalhes
│   ├── chat.html                 # ⭐ PÁGINA PRINCIPAL
│   ├── relatorios.html           # Relatórios
│   ├── prazos.html               # Agenda
│   ├── perfil.html
│   ├── configuracoes.html
│   │
│   ├── assets/
│   │   ├── logo-lawflake.svg     # Logo principal
│   │   ├── logo-lawflake-white.svg
│   │   └── favicon.ico
│   │
│   ├── css/
│   │   ├── lawflake.css          # Estilos principais
│   │   ├── components.css        # Componentes reutilizáveis
│   │   └── pages/
│   │       ├── dashboard.css
│   │       ├── chat.css          # ⭐ MAIS IMPORTANTE
│   │       └── processos.css
│   │
│   ├── js/
│   │   ├── config.js             # API URLs
│   │   ├── auth.js               # Supabase auth
│   │   ├── api.js                # HTTP client
│   │   ├── utils.js              # Helpers
│   │   │
│   │   ├── services/
│   │   │   ├── processo-service.js
│   │   │   ├── chat-service.js
│   │   │   ├── quick-actions-service.js
│   │   │   └── relatorio-service.js
│   │   │
│   │   ├── components/
│   │   │   ├── processo-card.js
│   │   │   ├── quick-action-btn.js
│   │   │   ├── source-citation.js
│   │   │   └── context-bar.js
│   │   │
│   │   └── pages/
│   │       ├── dashboard.js
│   │       ├── chat.js           # ⭐ MAIS IMPORTANTE
│   │       └── processos.js
│   │
│   └── components/
│       └── navbar.html           # Navbar reutilizável
│
├── vercel.json                   # Config Vercel
├── FRONTEND_PLAN.md              # Plano detalhado
├── README.md
└── START_PROMPT.md               # Este arquivo
```

---

## DOCUMENTAÇÃO DISPONÍVEL

No repositório frontend:
- `README.md` - Visão geral frontend
- `FRONTEND_PLAN.md` - Plano COMPLETO com wireframes, componentes, flows (60 páginas!)
- `START_PROMPT.md` - Este arquivo

No repositório backend:
- `IMPLEMENTATION_PLAN.md` - Referência de API endpoints
- `SNOWFLAKE_STRATEGY.md` - Como Quick Actions funcionam

---

## FASE ATUAL: FOUNDATION (SPRINT 1)

Estamos no **Sprint 1**: Foundation (3 dias)

### Objetivos desta fase:

1. **Setup inicial**
   - [ ] Estrutura de pastas
   - [ ] Config (`js/config.js`)
   - [ ] Assets (logo, favicon)

2. **CSS Base**
   - [ ] `css/lawflake.css` (variáveis, typography, layout)
   - [ ] `css/components.css` (cards, botões, badges)
   - [ ] Importar Bootstrap 5 (CDN)
   - [ ] Importar Bootstrap Icons (CDN)
   - [ ] Importar Google Fonts (Merriweather + Inter)

3. **Componentes Reutilizáveis**
   - [ ] Navbar (`components/navbar.html`)
   - [ ] Footer (opcional)

4. **Login Page**
   - [ ] `login.html` (layout profissional)
   - [ ] `js/auth.js` (Supabase auth integration)
   - [ ] Funcional: login → redirect dashboard

5. **Dashboard**
   - [ ] `dashboard.html` (layout com cards)
   - [ ] `js/pages/dashboard.js` (carregar stats)
   - [ ] 6 cards de estatísticas (mock data OK por agora)

---

## PÁGINA MAIS IMPORTANTE: CHAT

**O chat é o coração do LawFlake.** 80% do tempo do usuário será aqui.

### Layout Essencial

```
┌─────────────────────────────────────────────────┐
│ Navbar                           [Prazos: 3]    │
├─────────────────────────────────────────────────┤
│                                                  │
│ 💬 CONSULTAR IA                                 │
│                                                  │
│ Olá, Dr. João. Como posso ajudar hoje?          │
│                                                  │
│ ┌─────────────────┐  ┌─────────────────┐       │
│ │ 📂 Processo     │  │ 📚 Todos os     │       │
│ │    Específico   │  │    Processos    │       │
│ └─────────────────┘  └─────────────────┘       │
│                                                  │
│ ⚡ AÇÕES RÁPIDAS:                                │
│ ┌───────┐ ┌───────┐ ┌───────┐                  │
│ │ ⏰    │ │ 🔴    │ │ 📊    │                  │
│ │ Prazos│ │ Crític│ │ Dashb.│                  │
│ └───────┘ └───────┘ └───────┘                  │
│                                                  │
│ 💬 Ou digite sua pergunta:                      │
│ ┌────────────────────────────────────────────┐ │
│ │ Ex: "Status do processo 0001234..."       │ │
│ └────────────────────────────────────────────┘ │
│                              [ Enviar ]         │
│                                                  │
└─────────────────────────────────────────────────┘
```

### Fluxo: Processo Selecionado

```
┌─────────────────────────────────────────────────┐
│ 📄 Processo: 0001234-56.2023.5.02.0001          │
│ 👤 Maria Silva vs Empresa XYZ                   │
│ 🔴 Risco: Alto | 💰 R$ 250.000,00               │
├─────────────────────────────────────────────────┤
│                                                  │
│ ⚡ O QUE VOCÊ PRECISA SABER?                     │
│                                                  │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│ │ 📄 RESUMO│ │ ⏰ PRAZOS│ │ ⚠️ RISCOS│         │
│ └──────────┘ └──────────┘ └──────────┘         │
│                                                  │
│ ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│ │ 📊 LINHA │ │ ⚖️ PREC. │ │ 📤 EXPOR.│         │
│ └──────────┘ └──────────┘ └──────────┘         │
│                                                  │
│ 💬 Ou pergunte livremente:                      │
│ [Qual foi a última movimentação?____]           │
│                              [ Enviar ]         │
└─────────────────────────────────────────────────┘
```

### Resposta com Sources

```
┌─────────────────────────────────────────────────┐
│ 🤖 LawFlake AI:                     10:45       │
│                                                  │
│ A última movimentação foi em **15/10/2025**:    │
│                                                  │
│ 📄 Juntada de Contestação pela ré (Empresa XYZ),│
│ alegando prescrição quinquenal.                  │
│                                                  │
│ ⏰ Próximo prazo: 30/10/2025 (3 dias)           │
│                                                  │
│ 📎 FONTES:                                       │
│ ┌────────────────────────────────────────────┐ │
│ │ 📄 Contestação (15/10/2025)      [Abrir]  │ │
│ │    Página 3 • Confidence: 95%             │ │
│ ├────────────────────────────────────────────┤ │
│ │ 📄 Despacho (16/10/2025)         [Abrir]  │ │
│ │    Prazo para manifestação                │ │
│ └────────────────────────────────────────────┘ │
│                                                  │
│ ℹ️ Esta resposta foi gerada por IA.             │
│ Sempre revise os documentos originais.          │
└─────────────────────────────────────────────────┘
```

---

## COMPONENTES REUTILIZÁVEIS

### 1. QuickActionButton

```html
<button class="quick-action-btn" data-action="resumo-executivo">
  <div class="quick-action-icon">
    <i class="bi bi-file-earmark-text fs-3"></i>
  </div>
  <div class="quick-action-label">
    Resumo Executivo
  </div>
</button>
```

```css
.quick-action-btn {
  border: 2px solid var(--lawflake-border);
  border-radius: 12px;
  padding: 1.5rem;
  background: white;
  transition: all 0.2s;
  cursor: pointer;
  text-align: center;
  width: 100%;
}

.quick-action-btn:hover {
  border-color: var(--lawflake-primary);
  box-shadow: 0 4px 12px rgba(30, 58, 95, 0.15);
  transform: translateY(-2px);
}
```

### 2. SourceCitation

```html
<div class="source-citation">
  <div class="d-flex align-items-start">
    <div class="source-icon me-2">
      <i class="bi bi-file-earmark-text text-primary"></i>
    </div>
    <div class="flex-grow-1">
      <div class="source-title">
        <strong>Contestação</strong> • 15/10/2025
      </div>
      <div class="source-detail text-muted small">
        Página 3, parágrafo 12 • Confidence: 95%
      </div>
    </div>
    <button class="btn btn-sm btn-outline-primary">Abrir</button>
  </div>
</div>
```

### 3. ContextBar

```html
<div class="context-bar">
  <div class="d-flex justify-content-between align-items-center">
    <div>
      <div class="context-title">
        📄 Processo: 0001234-56.2023.5.02.0001
      </div>
      <div class="context-subtitle">
        👤 Maria Silva vs Empresa XYZ Ltda
      </div>
    </div>
    <div class="context-badges">
      <span class="badge bg-danger">🔴 Alto Risco</span>
      <span class="badge bg-secondary">💰 R$ 250.000,00</span>
    </div>
  </div>
</div>
```

```css
.context-bar {
  background: linear-gradient(135deg, var(--lawflake-primary), var(--lawflake-secondary));
  color: white;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  margin-bottom: 1.5rem;
}

.context-title {
  font-weight: 600;
  font-size: 1rem;
}

.context-subtitle {
  font-size: 0.9rem;
  opacity: 0.9;
}
```

### 4. ProcessoCard

```html
<div class="processo-card card shadow-sm border-start border-5 border-danger">
  <div class="card-body">
    <div class="d-flex justify-content-between">
      <div class="flex-grow-1">
        <h6 class="card-title mb-1">
          <span class="badge bg-danger me-2">🔴 Alto</span>
          0001234-56.2023.5.02.0001
        </h6>
        <p class="card-text text-muted small mb-2">
          <strong>Silva vs XYZ</strong> • TRT-2 São Paulo
        </p>
        <p class="card-text small mb-0">
          Valor: <strong>R$ 250.000,00</strong> •
          Prazo: <span class="text-danger">3 dias</span>
        </p>
      </div>
      <div class="dropdown">
        <button class="btn btn-sm btn-link" data-bs-toggle="dropdown">
          <i class="bi bi-three-dots-vertical"></i>
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#">Ver detalhes</a></li>
          <li><a class="dropdown-item" href="#">Consultar IA</a></li>
          <li><a class="dropdown-item" href="#">Exportar</a></li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

---

## INTEGRAÇÃO COM BACKEND

### Config (`js/config.js`)

```javascript
const config = {
    // API Backend
    API_URL: window.location.hostname === 'localhost'
        ? 'http://localhost:8000'
        : 'https://lawflake-production.up.railway.app',

    // Supabase Auth
    SUPABASE_URL: 'https://bydfdmmyzjdsfaomhwse.supabase.co',
    SUPABASE_ANON_KEY: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ5ZGZkbW15empkc2Zhb21od3NlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjExMzA2MTIsImV4cCI6MjA3NjcwNjYxMn0.J1Ju2irp4qSPZWM4HwY8ZcIMo7kW6qchSGoa3XNShIE',

    // App
    APP_NAME: 'LawFlake',
    VERSION: '1.0.0'
};
```

### HTTP Client (`js/api.js`)

```javascript
class APIClient {
    constructor() {
        this.baseURL = config.API_URL;
    }

    getToken() {
        return localStorage.getItem('access_token');
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseURL}${endpoint}`;
        const headers = {
            'Content-Type': 'application/json',
            ...options.headers
        };

        const token = this.getToken();
        if (token) {
            headers['Authorization'] = `Bearer ${token}`;
        }

        const response = await fetch(url, {
            ...options,
            headers
        });

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        return response.json();
    }

    async get(endpoint) {
        return this.request(endpoint);
    }

    async post(endpoint, data) {
        return this.request(endpoint, {
            method: 'POST',
            body: JSON.stringify(data)
        });
    }

    async put(endpoint, data) {
        return this.request(endpoint, {
            method: 'PUT',
            body: JSON.stringify(data)
        });
    }

    async delete(endpoint) {
        return this.request(endpoint, {
            method: 'DELETE'
        });
    }
}

const api = new APIClient();
```

### Auth (`js/auth.js`)

```javascript
// Supabase client
const supabase = window.supabase.createClient(
    config.SUPABASE_URL,
    config.SUPABASE_ANON_KEY
);

// Login
async function login(email, password) {
    const { data, error } = await supabase.auth.signInWithPassword({
        email,
        password
    });

    if (error) throw error;

    // Save token
    localStorage.setItem('access_token', data.session.access_token);
    localStorage.setItem('user', JSON.stringify(data.user));

    return data;
}

// Logout
async function logout() {
    await supabase.auth.signOut();
    localStorage.removeItem('access_token');
    localStorage.removeItem('user');
    window.location.href = '/login.html';
}

// Check auth
function isAuthenticated() {
    return !!localStorage.getItem('access_token');
}

// Protect page
function requireAuth() {
    if (!isAuthenticated()) {
        window.location.href = '/login.html';
    }
}
```

---

## PRÓXIMOS PASSOS (O QUE FAZER AGORA)

### 1. Setup Inicial (30min)
- [ ] Criar estrutura de pastas (`public/`, `css/`, `js/`)
- [ ] Criar `index.html` (redirect para login)
- [ ] Criar `vercel.json` (config deploy)

### 2. CSS Base (1h)
- [ ] Criar `css/lawflake.css` (variáveis, reset, typography)
- [ ] Importar CDNs (Bootstrap, Icons, Fonts)
- [ ] Testar: página HTML simples com estilos

### 3. Config & Utils (30min)
- [ ] Criar `js/config.js` (URLs, keys)
- [ ] Criar `js/api.js` (HTTP client)
- [ ] Criar `js/auth.js` (Supabase auth)
- [ ] Criar `js/utils.js` (helpers: formatDate, formatCurrency, etc)

### 4. Login Page (1h)
- [ ] Criar `login.html` (layout profissional)
- [ ] Form de login funcional
- [ ] Integrar Supabase auth
- [ ] Testar: login → redirect dashboard

### 5. Navbar Component (30min)
- [ ] Criar `components/navbar.html`
- [ ] Links para páginas principais
- [ ] Badge de alertas de prazos
- [ ] Dropdown de usuário

### 6. Dashboard (1h)
- [ ] Criar `dashboard.html`
- [ ] 6 cards de estatísticas
- [ ] Incluir navbar
- [ ] Carregar dados (mock OK por agora)
- [ ] Testar: auth → dashboard carrega

---

## CRITÉRIOS DE SUCESSO (SPRINT 1)

✅ Estrutura de pastas criada
✅ CSS base funcionando (variáveis, Bootstrap)
✅ Login funcional (Supabase auth)
✅ Dashboard carrega com cards (pode ser mock data)
✅ Navbar reutilizável funcionando
✅ API client configurado
✅ Deploy na Vercel funcionando

---

## O QUE NÃO FAZER

❌ **NÃO** usar frameworks (React, Vue) - apenas Vanilla JS
❌ **NÃO** criar chat agora (Sprint 2)
❌ **NÃO** usar cores "fofas" ou informais
❌ **NÃO** copiar UI do Project Guru (domínio diferente)
❌ **NÃO** fazer mobile-first (desktop é prioridade)

---

## REFERÊNCIAS RÁPIDAS

### CDNs para incluir

```html
<!-- Bootstrap CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- Bootstrap Icons -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">

<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Merriweather:wght@700;900&display=swap" rel="stylesheet">

<!-- Bootstrap JS + Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

<!-- Supabase -->
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>

<!-- Chart.js (para dashboard) -->
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
```

### Template HTML Base

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LawFlake - Intelligence for Legal Work</title>

    <!-- Favicon -->
    <link rel="icon" type="image/x-icon" href="/assets/favicon.ico">

    <!-- CDNs -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.1/font/bootstrap-icons.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Merriweather:wght@700;900&display=swap" rel="stylesheet">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="/css/lawflake.css">
    <link rel="stylesheet" href="/css/components.css">
</head>
<body>

    <!-- Navbar aqui -->

    <!-- Content aqui -->

    <!-- Scripts -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
    <script src="/js/config.js"></script>
    <script src="/js/api.js"></script>
    <script src="/js/auth.js"></script>
    <script src="/js/utils.js"></script>
</body>
</html>
```

---

## COMANDO PARA COMEÇAR

Agora você pode começar! Inicie dizendo:

**"Vou começar a implementar o LawFlake frontend - SPRINT 1: Foundation. Vou criar a estrutura inicial e a página de login."**

E siga os próximos passos acima. 🚀

---

**LawFlake Frontend - Profissionalismo em cada pixel.** 🏛️
