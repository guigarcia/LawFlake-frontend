# 🏛️ LawFlake Frontend

**Interface profissional para advogados empresariais**

---

## 📖 VISÃO GERAL

Frontend do LawFlake - sistema de inteligência processual jurídica com foco em **Quick Actions** e chat com IA.

**Princípios de Design**:
- ✅ Seriedade e profissionalismo
- ✅ Desktop-first (advogados trabalham em computadores)
- ✅ Quick Actions como protagonistas (não chat livre)
- ✅ Sources sempre visíveis
- ✅ Máximo 2 cliques para qualquer ação

---

## 🎨 IDENTIDADE VISUAL

### Cores

```css
--lawflake-primary: #1e3a5f;      /* Azul escuro profissional */
--lawflake-secondary: #2c5f8d;    /* Azul médio */
--lawflake-accent: #d4af37;       /* Dourado (elegância) */

--lawflake-success: #2d5016;      /* Verde escuro */
--lawflake-warning: #8b6914;      /* Amarelo escuro */
--lawflake-danger: #8b1a1a;       /* Vermelho escuro */
```

### Tipografia

- **Títulos**: Merriweather (serif) - elegância
- **Corpo**: Inter (sans-serif) - legibilidade
- **Código**: JetBrains Mono (monospace)

### Ícones

Bootstrap Icons (consistência com Bootstrap 5)

---

## 📂 ESTRUTURA

```
lawflake-frontend/
├── public/
│   ├── index.html                # Redirect para login
│   ├── login.html                # Autenticação
│   ├── dashboard.html            # Dashboard principal
│   ├── processos.html            # Lista de processos
│   ├── processo-detalhe.html     # Detalhes do processo
│   ├── chat.html                 # Chat com IA (PRINCIPAL)
│   ├── relatorios.html           # Geração de relatórios
│   ├── prazos.html               # Agenda de prazos
│   ├── perfil.html               # Perfil do usuário
│   ├── configuracoes.html        # Configurações
│   │
│   ├── assets/
│   │   ├── logo-lawflake.svg
│   │   └── images/
│   │
│   ├── css/
│   │   ├── lawflake.css          # Estilos principais
│   │   ├── components.css        # Componentes reutilizáveis
│   │   └── pages/                # Estilos por página
│   │
│   ├── js/
│   │   ├── config.js             # Configurações (API URL)
│   │   ├── auth.js               # Autenticação Supabase
│   │   ├── api.js                # Client HTTP
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
│   │       ├── chat.js           # MAIS IMPORTANTE
│   │       ├── processos.js
│   │       └── processo-detalhe.js
│   │
│   └── components/
│       ├── navbar.html           # Navbar reutilizável
│       └── footer.html
│
├── vercel.json                   # Configuração Vercel
├── FRONTEND_PLAN.md              # Plano detalhado
└── README.md                     # Este arquivo
```

---

## 🚀 TECNOLOGIAS

- **Vanilla JavaScript** (ES6+, sem frameworks)
- **Bootstrap 5.3** (UI components)
- **Bootstrap Icons** (ícones)
- **Chart.js** (gráficos)
- **Supabase JS** (auth)
- **Marked.js** (markdown rendering)
- **DOMPurify** (XSS protection)

**Por que Vanilla JS?**
- Mais simples (sem build step)
- Mais rápido (sem bundle)
- Mais fácil manutenção
- Menos dependências

---

## 📄 PÁGINAS PRINCIPAIS

### 1. **Dashboard** (`dashboard.html`)

```
┌────────────────────────────────────────────┐
│ Stats Cards (6):                            │
│ - Críticos | Urgentes | Total              │
│ - Exposição | Próximo Prazo | Taxa Sucesso │
├────────────────────────────────────────────┤
│ Processos Críticos (Tabela top-5)          │
├────────────────────────────────────────────┤
│ Gráficos:                                   │
│ - Processos por tipo (pizza)               │
│ - Timeline mensal (linha)                  │
└────────────────────────────────────────────┘
```

### 2. **Chat** (`chat.html`) ⭐ **MAIS IMPORTANTE**

```
┌────────────────────────────────────────────┐
│ Seletor: [Processo Específico] [Todos]     │
├────────────────────────────────────────────┤
│ Context Bar (quando processo selecionado): │
│ - Nº processo, partes, foro, valor, risco  │
├────────────────────────────────────────────┤
│ QUICK ACTIONS (Botões grandes):            │
│ [Resumo]  [Prazos]  [Riscos]              │
│ [Timeline]  [Precedentes]  [Exportar]      │
├────────────────────────────────────────────┤
│ Chat Messages:                              │
│ - Usuário: pergunta                         │
│ - LawFlake AI: resposta + sources          │
├────────────────────────────────────────────┤
│ Input: [Digite sua pergunta...] [Enviar]   │
└────────────────────────────────────────────┘
```

**Features essenciais**:
- Context Bar sempre visível
- Sources clicáveis em cada resposta
- Confidence score exibido
- Disclaimer em cada resposta
- Typing indicator
- Copy/Export conversation

### 3. **Processos** (`processos.html`)

```
┌──────────┬─────────────────────────────────┐
│ FILTROS  │ Lista de Processos (Tabela)     │
│          │                                 │
│ Busca    │ Nº | Partes | Foro | Valor | 🔴│
│ Tipo     │ Sortable, filterable            │
│ Foro     │                                 │
│ Risco    │ Ações inline: Ver, Chat, Export │
│ Valor    │                                 │
└──────────┴─────────────────────────────────┘
```

### 4. **Detalhes do Processo** (`processo-detalhe.html`)

```
┌──────────┬─────────────────────────────────┐
│ MENU     │ Identificação                    │
│          │ - Nº, tipo, foro, partes, valor │
│ Resumo   ├─────────────────────────────────┤
│ Timeline │ Timeline (Movimentações)         │
│ Docs     │ - Cronológica, com documentos   │
│ Partes   ├─────────────────────────────────┤
│ Prazos   │ Próximos Prazos                  │
│ Riscos   │ - Lista com urgência            │
│ Ações    ├─────────────────────────────────┤
│          │ Análise de Risco                 │
│ [Export] │ - Score, fatores, recomendações │
└──────────┴─────────────────────────────────┘
```

---

## ⚡ COMPONENTES REUTILIZÁVEIS

### `ProcessoCard`

Card de processo para listas:

```html
<div class="processo-card">
  <span class="badge bg-danger">🔴 Alto</span>
  <h6>0001234-56.2023.5.02.0001</h6>
  <p>Silva vs XYZ • TRT-2 São Paulo</p>
  <p>Valor: R$ 250k • Prazo: 3 dias</p>
  <div class="actions">
    [Ver] [Chat] [Export]
  </div>
</div>
```

### `QuickActionButton`

Botão de ação rápida:

```html
<button class="quick-action-btn" data-action="resumo">
  <i class="bi bi-file-earmark-text"></i>
  <span>Resumo Executivo</span>
</button>
```

### `SourceCitation`

Citação de fonte:

```html
<div class="source-citation">
  <i class="bi bi-file-earmark-text"></i>
  <div>
    <strong>Contestação</strong> • 15/10/2025
    <small>Página 3 • Confidence: 95%</small>
  </div>
  <button>Abrir</button>
</div>
```

### `ContextBar`

Barra de contexto do processo (no chat):

```html
<div class="context-bar">
  📄 Processo: 0001234-56.2023.5.02.0001
  👤 Maria Silva vs Empresa XYZ Ltda
  🏛️ TRT-2 (São Paulo) | ⚖️ Trabalhista
  🔴 Risco: Alto | 💰 R$ 250.000,00
</div>
```

---

## 🎯 FLUXO DE USUÁRIO (CHAT)

### 1. Entrar no Chat

```
Olá, Dr. João. Como posso ajudar hoje?

[📂 Processo Específico]  [📚 Todos os Processos]

⚡ AÇÕES RÁPIDAS:
[⏰ Prazos]  [🔴 Críticos]  [📊 Dashboard]
```

### 2. Selecionar "Processo Específico"

```
🔍 Buscar Processo
[Digite número, partes ou palavras-chave_______]

📋 Processos recentes:
• 0001234-56 - Silva vs XYZ (TRT-2)
• 0002345-67 - Costa vs ABC (TJSP)
```

### 3. Processo Selecionado → Quick Actions

```
📄 Processo: 0001234-56.2023.5.02.0001
👤 Maria Silva vs Empresa XYZ Ltda
🔴 Risco: Alto | 💰 R$ 250.000,00

⚡ O QUE VOCÊ PRECISA SABER?

[📄 RESUMO]  [⏰ PRAZOS]  [⚠️ RISCOS]
[📊 LINHA DO TEMPO]  [⚖️ PRECEDENTES]  [📤 EXPORTAR]

💬 Ou pergunte livremente:
[Qual foi a última movimentação?_____] [Enviar]
```

### 4. Quick Action → Resposta Estruturada

```
🤖 LawFlake AI:

📄 RESUMO EXECUTIVO

IDENTIFICAÇÃO
• Processo: 0001234-56.2023.5.02.0001
• Autor: Maria Silva
• Réu: Empresa XYZ Ltda
• Vara: 1ª Vara do Trabalho de São Paulo

STATUS ATUAL
• Fase: Contestação
• Última movimentação: 15/10/2025
  "Juntada de Contestação pela ré"

RISCO
• Classificação: 🔴 Alto (Score: 75/100)
• Justificativa:
  - Valor elevado (R$ 250k)
  - Jurisprudência desfavorável no TRT-2
  - Prazo vencendo em 3 dias

PRÓXIMOS PASSOS
• 30/10/2025 (3 dias): Manifestação sobre contestação
• 15/11/2025 (18 dias): Audiência preliminar

📎 FONTES:
┌──────────────────────────────────┐
│ 📄 Contestação (15/10/2025)      │
│    Página 3 • Confidence: 95%    │
│    [Abrir]                        │
├──────────────────────────────────┤
│ 📄 Despacho (16/10/2025)         │
│    Prazo para manifestação       │
│    [Abrir]                        │
└──────────────────────────────────┘

ℹ️ Esta resposta foi gerada por IA. Sempre revise os
documentos originais.
```

---

## 🔌 INTEGRAÇÃO COM BACKEND

### Configuração (`js/config.js`)

```javascript
const config = {
    API_URL: 'https://lawflake-backend.railway.app',
    SUPABASE_URL: 'https://xxx.supabase.co',
    SUPABASE_ANON_KEY: 'eyJxxx...'
};
```

### Client HTTP (`js/api.js`)

```javascript
class APIClient {
    constructor() {
        this.baseURL = config.API_URL;
        this.token = localStorage.getItem('access_token');
    }

    async get(endpoint) {
        const response = await fetch(`${this.baseURL}${endpoint}`, {
            headers: {
                'Authorization': `Bearer ${this.token}`
            }
        });
        return response.json();
    }

    async post(endpoint, data) {
        const response = await fetch(`${this.baseURL}${endpoint}`, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${this.token}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        return response.json();
    }
}

const api = new APIClient();
```

### Exemplo de uso (`js/services/quick-actions-service.js`)

```javascript
async function gerarResumoExecutivo(processoId) {
    try {
        showLoading('Gerando resumo...');

        const response = await api.post('/api/v1/quick-actions/resumo-executivo', {
            processo_id: processoId
        });

        hideLoading();
        renderResumoExecutivo(response);

    } catch (error) {
        hideLoading();
        showError('Erro ao gerar resumo: ' + error.message);
    }
}
```

---

## 🎨 ESTILOS PRINCIPAIS

### `css/lawflake.css`

```css
:root {
    --lawflake-primary: #1e3a5f;
    --lawflake-accent: #d4af37;
    /* ... outras variáveis ... */
}

body {
    font-family: 'Inter', sans-serif;
    color: var(--lawflake-text);
    background: var(--lawflake-bg);
}

h1, h2, h3 {
    font-family: 'Merriweather', serif;
    color: var(--lawflake-primary);
}

.quick-action-btn {
    border: 2px solid var(--lawflake-border);
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.2s;
}

.quick-action-btn:hover {
    border-color: var(--lawflake-primary);
    box-shadow: var(--lawflake-shadow);
    transform: translateY(-2px);
}

.source-citation {
    border-left: 3px solid var(--lawflake-primary);
    padding: 0.75rem;
    background: #f8f9fa;
    margin: 0.5rem 0;
}

.context-bar {
    background: linear-gradient(135deg, var(--lawflake-primary), var(--lawflake-secondary));
    color: white;
    padding: 1rem;
    border-radius: 8px;
    margin-bottom: 1rem;
}
```

---

## 🧪 TESTES E VALIDAÇÃO

### Checklist de Qualidade

Cada página deve:
- [ ] Carregar em < 2s
- [ ] Funcionar sem JavaScript (graceful degradation)
- [ ] Ser responsiva (mobile + desktop)
- [ ] Ter loading states para ações async
- [ ] Ter error handling visual
- [ ] Ser acessível (ARIA labels, keyboard navigation)
- [ ] Não ter console errors

### Testes Manuais

1. **Login Flow**
   - Login com credenciais corretas → sucesso
   - Login com credenciais erradas → erro legível
   - Logout → redirect para login

2. **Dashboard**
   - Cards carregam dados reais
   - Gráficos renderizam corretamente
   - Links funcionam

3. **Chat** (CRÍTICO)
   - Seletor funciona
   - Quick Actions executam e retornam resultados
   - Sources são clicáveis
   - Chat livre funciona
   - Typing indicator aparece durante loading

4. **Processos**
   - Lista carrega
   - Filtros funcionam
   - Sort funciona
   - Ações inline funcionam

---

## 🚀 DEPLOY (VERCEL)

### Setup

1. Conectar repo GitHub com Vercel
2. Configurar environment variables:
   - `VITE_API_URL`
   - `VITE_SUPABASE_URL`
   - `VITE_SUPABASE_ANON_KEY`
3. Push para `main` → deploy automático

### `vercel.json`

```json
{
  "version": 2,
  "builds": [
    { "src": "public/**", "use": "@vercel/static" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "/public/$1" },
    { "src": "/", "dest": "/public/index.html" }
  ]
}
```

---

## 📋 PRIORIDADES DE IMPLEMENTAÇÃO

### Sprint 1 (3 dias): Foundation
- [ ] Login page + auth Supabase
- [ ] Dashboard layout + cards
- [ ] Navbar component
- [ ] API client

### Sprint 2 (4 dias): Chat (PRIORIDADE)
- [ ] Chat layout completo
- [ ] Context Bar component
- [ ] Quick Actions buttons (UI)
- [ ] Quick Actions integration (API calls)
- [ ] Sources display
- [ ] Chat livre

### Sprint 3 (2 dias): Processos & Detalhes
- [ ] Lista de processos
- [ ] Filtros
- [ ] Página de detalhes
- [ ] Timeline

### Sprint 4 (1 dia): Polish
- [ ] Responsividade
- [ ] Animações
- [ ] Error handling
- [ ] Acessibilidade

---

## 📚 DOCUMENTAÇÃO

- **[FRONTEND_PLAN.md](./FRONTEND_PLAN.md)**: Plano detalhado com wireframes, componentes, UX flows
- **[../LawFlake/README.md](../LawFlake/README.md)**: Visão geral do projeto
- **[../LawFlake/IMPLEMENTATION_PLAN.md](../LawFlake/IMPLEMENTATION_PLAN.md)**: Plano de backend

---

## 🎯 DEFINIÇÃO DE PRONTO

Frontend está pronto quando:
- [ ] Todas as páginas principais implementadas
- [ ] Chat funcional com Quick Actions
- [ ] Conectado ao backend real (não mock)
- [ ] Responsivo (mobile + desktop)
- [ ] Loading states e error handling
- [ ] Acessível (keyboard, screen readers)
- [ ] Testado em Chrome, Firefox, Safari
- [ ] Deploy na Vercel funcionando

---

**LawFlake Frontend - Profissionalismo em cada pixel. 🏛️**
