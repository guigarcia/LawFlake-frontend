# 🏛️ LawFlake Frontend - Plano de Implementação

**Data**: 2025-10-22
**Versão**: 1.0.0
**Stack**: Vanilla JS + Bootstrap 5 + Chart.js
**Deploy**: Vercel

---

## 🎯 PRINCÍPIOS DE DESIGN

### Para Advogados Empresariais

1. **Seriedade e Profissionalismo**
   - Cores sóbrias: azul escuro, cinza, branco
   - Tipografia: Serif para títulos (elegância), Sans-serif para corpo
   - Sem elementos "fofos" ou informais
   - Layout limpo, espaço em branco generoso

2. **Eficiência Acima de Tudo**
   - Informação crítica sempre visível (prazos, riscos)
   - Máximo 2 cliques para qualquer ação
   - Quick Actions como protagonistas
   - Keyboard shortcuts para power users

3. **Confiança e Transparência**
   - Sources SEMPRE visíveis e clicáveis
   - Confidence scores exibidos
   - Disclaimer jurídico presente
   - Audit trail acessível

4. **Responsividade**
   - Desktop-first (advogados usam computadores)
   - Mobile para consultas rápidas

---

## 🎨 IDENTIDADE VISUAL

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
--lawflake-info: #1e5a7d;         /* Azul info */

/* Neutros */
--lawflake-bg: #f8f9fa;           /* Fundo claro */
--lawflake-bg-dark: #2a2a2a;      /* Fundo escuro */
--lawflake-text: #2c3e50;         /* Texto principal */
--lawflake-text-muted: #6c757d;   /* Texto secundário */
--lawflake-border: #dee2e6;       /* Bordas */

/* Sombras */
--lawflake-shadow: 0 2px 8px rgba(30, 58, 95, 0.1);
--lawflake-shadow-lg: 0 4px 16px rgba(30, 58, 95, 0.15);
```

### Tipografia

```css
/* Fontes */
--lawflake-font-serif: 'Merriweather', 'Georgia', serif;
--lawflake-font-sans: 'Inter', 'Segoe UI', system-ui, sans-serif;
--lawflake-font-mono: 'JetBrains Mono', 'Consolas', monospace;

/* Tamanhos */
--lawflake-fs-xs: 0.75rem;   /* 12px */
--lawflake-fs-sm: 0.875rem;  /* 14px */
--lawflake-fs-base: 1rem;    /* 16px */
--lawflake-fs-lg: 1.125rem;  /* 18px */
--lawflake-fs-xl: 1.25rem;   /* 20px */
--lawflake-fs-2xl: 1.5rem;   /* 24px */
--lawflake-fs-3xl: 1.875rem; /* 30px */
--lawflake-fs-4xl: 2.25rem;  /* 36px */
```

### Ícones

**Biblioteca**: Bootstrap Icons (consistência)

**Ícones principais**:
- 📂 Processo: `bi-folder-fill`
- ⚖️ Jurídico: `bi-scale`
- ⏰ Prazos: `bi-alarm`
- 🔴 Risco: `bi-exclamation-triangle-fill`
- 📊 Analytics: `bi-bar-chart-line`
- 📄 Documento: `bi-file-earmark-text`
- 💬 Chat: `bi-chat-dots`
- 🔍 Busca: `bi-search`
- ⚙️ Config: `bi-gear`
- 👤 Perfil: `bi-person-circle`

---

## 📐 LAYOUT E ESTRUTURA

### Header (Navbar)

```html
<nav class="navbar navbar-expand-lg navbar-dark bg-lawflake-primary fixed-top">
  <div class="container-fluid px-4">
    <!-- Logo -->
    <a class="navbar-brand d-flex align-items-center" href="/dashboard.html">
      <img src="/assets/logo-lawflake.svg" height="36" alt="LawFlake">
      <span class="ms-2 fs-5 fw-bold">LawFlake</span>
    </a>

    <!-- Main Nav -->
    <div class="collapse navbar-collapse" id="navbarMain">
      <ul class="navbar-nav ms-auto me-3">
        <li class="nav-item">
          <a class="nav-link" href="/dashboard.html">
            <i class="bi bi-speedometer2"></i> Dashboard
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/processos.html">
            <i class="bi bi-folder-fill"></i> Processos
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/chat.html">
            <i class="bi bi-chat-dots"></i> Consultar IA
          </a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="/relatorios.html">
            <i class="bi bi-file-earmark-bar-graph"></i> Relatórios
          </a>
        </li>
      </ul>

      <!-- Alerts Badge -->
      <div class="me-3">
        <a href="/prazos.html" class="btn btn-sm btn-warning position-relative">
          <i class="bi bi-alarm"></i> Prazos
          <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
            3
          </span>
        </a>
      </div>

      <!-- User Dropdown -->
      <div class="dropdown">
        <button class="btn btn-link text-white dropdown-toggle" data-bs-toggle="dropdown">
          <i class="bi bi-person-circle fs-5"></i>
          <span id="userName" class="ms-1">Dr. João</span>
        </button>
        <ul class="dropdown-menu dropdown-menu-end">
          <li><a class="dropdown-item" href="/perfil.html">Perfil</a></li>
          <li><a class="dropdown-item" href="/configuracoes.html">Configurações</a></li>
          <li><hr class="dropdown-divider"></li>
          <li><a class="dropdown-item" onclick="logout()">Sair</a></li>
        </ul>
      </div>
    </div>
  </div>
</nav>
```

### Sidebar (Opcional para algumas páginas)

- Dashboard: Sem sidebar (cards full)
- Processos: Sidebar com filtros
- Chat: Sidebar com sessões de chat
- Detalhes do Processo: Sidebar com timeline

---

## 📄 PÁGINAS E COMPONENTES

### 1. **Login (`login.html`)**

**Layout**:
```
┌────────────────────────────────────────┐
│                                        │
│            [Logo LawFlake]             │
│                                        │
│    ┌──────────────────────────────┐   │
│    │  Acesso ao Sistema Jurídico  │   │
│    │                              │   │
│    │  Email: [____________]       │   │
│    │  Senha: [____________]       │   │
│    │                              │   │
│    │  [ Entrar ]                  │   │
│    │                              │   │
│    │  Esqueceu a senha?           │   │
│    └──────────────────────────────┘   │
│                                        │
│  © 2025 LawFlake - Sistema seguro     │
│  Todos os dados são criptografados    │
└────────────────────────────────────────┘
```

**Características**:
- Background: gradiente azul escuro sutil
- Card centralizado com sombra
- Logo dourado/branco
- Ícone de cadeado (segurança)
- Link para "Primeiro acesso"

### 2. **Dashboard (`dashboard.html`)**

**Layout**:
```
┌─────────────────────────────────────────────────────────┐
│ Navbar                                     [Prazos: 3]  │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Bem-vindo, Dr. João Silva                    [Config]  │
│  Escritório: Silva & Associados                          │
│                                                          │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐          │
│  │ 🔴 CRÍTICO │ │ ⚠️ URGENTE │ │ 📂 TOTAL   │          │
│  │     3      │ │     8      │ │   127      │          │
│  │ processos  │ │ processos  │ │ processos  │          │
│  └────────────┘ └────────────┘ └────────────┘          │
│                                                          │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐          │
│  │ 💰 EXPOSI. │ │ ⏰ PRAZOS  │ │ 📊 SUCESSO │          │
│  │ R$ 12,3M   │ │  5 dias    │ │   78%      │          │
│  │ total      │ │ próximo    │ │ taxa       │          │
│  └────────────┘ └────────────┘ └────────────┘          │
│                                                          │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                          │
│  🔴 PROCESSOS CRÍTICOS (Requerem atenção imediata)      │
│  ┌────────────────────────────────────────────────────┐ │
│  │ 0001234-56  │ Silva vs XYZ  │ TRT-2 │ R$ 500k │ 🔴│ │
│  │ Prazo: 3 dias │ Recurso pendente │ [Ver] [Ação] │   │
│  ├────────────────────────────────────────────────────┤ │
│  │ 0002345-67  │ Costa vs ABC  │ TJSP  │ R$ 300k │ 🔴│ │
│  │ Prazo: 5 dias │ Audiência     │ [Ver] [Ação]  │   │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  📊 ANALYTICS                                            │
│  [Gráfico de processos por tipo]  [Timeline mensal]     │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Componentes**:
1. **Stats Cards** (6 cards principais)
   - Número grande e destacado
   - Ícone representativo
   - Variação (↑↓) se aplicável
   - Clicável para filtrar

2. **Tabela de Processos Críticos**
   - Top 5 processos com risco alto
   - Colunas: Número, Partes, Foro, Valor, Risco
   - Badge colorido para risco
   - Botões de ação inline

3. **Gráficos** (Chart.js)
   - Processos por tipo (pizza)
   - Timeline de movimentações (linha)
   - Distribuição de risco (barra)

4. **Quick Actions Globais**
   - Botão flutuante (FAB) no canto inferior direito
   - Menu radial com ações: "Novo Processo", "Consultar IA", "Gerar Relatório"

### 3. **Processos (`processos.html`)**

**Layout**:
```
┌─────────────────────────────────────────────────────────┐
│ Navbar                                                   │
├──────────┬──────────────────────────────────────────────┤
│          │                                              │
│ FILTROS  │  📂 PROCESSOS (127)        [+ Novo] [Export]│
│          │                                              │
│ 🔍 Busca │  ┌─────────────────────────────────────────┐│
│ [_____]  │  │ Nº       │ Partes │ Foro │ Valor │ Risco││
│          │  ├─────────────────────────────────────────┤│
│ Tipo     │  │ 0001234  │ Silva  │ TRT-2│ 500k  │ 🔴   ││
│ ☑ Trab.  │  │ 0002345  │ Costa  │ TJSP │ 300k  │ 🟡   ││
│ ☐ Civil  │  │ 0003456  │ Santos │ TRF-3│ 200k  │ 🟢   ││
│ ☐ Crim.  │  │ ...                                      ││
│          │  └─────────────────────────────────────────┘│
│ Foro     │                                              │
│ ☑ TRT-2  │  Paginação: [<] 1 2 3 ... 10 [>]            │
│ ☐ TJSP   │                                              │
│          │                                              │
│ Risco    │                                              │
│ ☑ Alto   │                                              │
│ ☑ Médio  │                                              │
│ ☐ Baixo  │                                              │
│          │                                              │
│ Valor    │                                              │
│ >500k ☑  │                                              │
│ 100-500k │                                              │
│          │                                              │
│ [Limpar] │                                              │
│          │                                              │
└──────────┴──────────────────────────────────────────────┘
```

**Features**:
- Filtros em tempo real (sem reload)
- Search com autocomplete
- Sort por coluna (clique no header)
- Ações inline: Ver, Editar, Exportar
- Bulk actions: Selecionar múltiplos → Exportar relatório consolidado
- Export CSV/Excel

### 4. **Chat / Consultar IA (`chat.html`)**

**PÁGINA MAIS IMPORTANTE - Prioridade máxima no design**

**Layout**:
```
┌─────────────────────────────────────────────────────────┐
│ Navbar                                                   │
├──────────┬──────────────────────────────────────────────┤
│          │                                              │
│ SESSÕES  │  💬 CONSULTAR IA                             │
│          │                                              │
│ + Nova   │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│          │                                              │
│ 📂 Geral │  Olá, Dr. João. Como posso ajudar hoje?     │
│ Silva vs │                                              │
│ Costa vs │  ┌──────────────────┐  ┌──────────────────┐ │
│ Santos   │  │ 📂 Processo      │  │ 📚 Todos os      │ │
│          │  │    Específico    │  │    Processos     │ │
│ [...]    │  └──────────────────┘  └──────────────────┘ │
│          │                                              │
│          │  ⚡ AÇÕES RÁPIDAS:                           │
│          │  ┌────────┐ ┌────────┐ ┌────────┐          │
│          │  │ ⏰     │ │ 🔴     │ │ 📊     │          │
│          │  │ Prazos │ │ Crític │ │ Dashb. │          │
│          │  └────────┘ └────────┘ └────────┘          │
│          │                                              │
│          │  💬 Ou digite sua pergunta:                 │
│          │  ┌────────────────────────────────────────┐ │
│          │  │ Ex: "Status do processo 0001234..."   │ │
│          │  └────────────────────────────────────────┘ │
│          │                                [ Enviar ]   │
│          │                                              │
└──────────┴──────────────────────────────────────────────┘
```

**Fluxo após selecionar "Processo Específico"**:
```
┌─────────────────────────────────────────────────────────┐
│ 💬 CONSULTAR IA                                          │
│                                                          │
│ ┌────────────────────────────────────────────────────┐  │
│ │ 🔍 Buscar Processo                                 │  │
│ │ [Digite número, partes ou palavras-chave_______]  │  │
│ │                                                    │  │
│ │ 📋 Processos recentes:                             │  │
│ │ • 0001234-56 - Silva vs XYZ (TRT-2)               │  │
│ │ • 0002345-67 - Costa vs ABC (TJSP)                │  │
│ └────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

**Após selecionar processo - Context Bar**:
```
┌─────────────────────────────────────────────────────────┐
│ 📄 Processo: 0001234-56.2023.5.02.0001                  │
│ 👤 Maria Silva vs Empresa XYZ Ltda                      │
│ 🏛️ TRT-2 (São Paulo) | ⚖️ Trabalhista                  │
│ 🔴 Risco: Alto | 💰 R$ 250.000,00 | ⏰ Prazo: 3 dias    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│ ⚡ O QUE VOCÊ PRECISA SABER?                             │
│                                                          │
│ ┌────────────┐ ┌────────────┐ ┌────────────┐           │
│ │ 📄 RESUMO  │ │ ⏰ PRAZOS  │ │ ⚠️ RISCOS  │           │
│ │ EXECUTIVO  │ │            │ │            │           │
│ └────────────┘ └────────────┘ └────────────┘           │
│                                                          │
│ ┌────────────┐ ┌────────────┐ ┌────────────┐           │
│ │ 📊 LINHA   │ │ ⚖️ PRECE-  │ │ 📤 EXPOR-  │           │
│ │ DO TEMPO   │ │ DENTES     │ │ TAR        │           │
│ └────────────┘ └────────────┘ └────────────┘           │
│                                                          │
│ 💬 Ou pergunte livremente:                              │
│ ┌──────────────────────────────────────────────────┐   │
│ │ [Qual foi a última movimentação?____________]    │   │
│ └──────────────────────────────────────────────────┘   │
│                                            [ Enviar ]   │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Resposta do Chat com Sources**:
```
┌─────────────────────────────────────────────────────────┐
│ 💬 CHAT - Silva vs XYZ (0001234-56)                     │
├─────────────────────────────────────────────────────────┤
│                                                          │
│ 👤 Você:                                      10:45     │
│ Qual foi a última movimentação?                         │
│                                                          │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                          │
│ 🤖 LawFlake AI:                               10:45     │
│                                                          │
│ A última movimentação foi em **15/10/2025**:            │
│                                                          │
│ 📄 **Juntada de Contestação** pela parte ré (Empresa   │
│ XYZ Ltda), alegando prescrição quinquenal e ausência    │
│ de nexo causal para dano moral.                         │
│                                                          │
│ ⏰ **Próximo prazo**: 30/10/2025 (em 3 dias) para      │
│ manifestação sobre a contestação.                        │
│                                                          │
│ 📎 **Fontes**:                                           │
│ ┌──────────────────────────────────────────────────┐   │
│ │ 📄 Contestação (15/10/2025)              [Abrir] │   │
│ │    Página 3, parágrafo 12                        │   │
│ │    Confidence: 95%                               │   │
│ ├──────────────────────────────────────────────────┤   │
│ │ 📄 Despacho (16/10/2025)                 [Abrir] │   │
│ │    Prazo para manifestação                       │   │
│ │    Confidence: 98%                               │   │
│ └──────────────────────────────────────────────────┘   │
│                                                          │
│ ℹ️ Esta resposta foi gerada por IA. Sempre revise os   │
│ documentos originais.                                    │
│                                                          │
│ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│                                                          │
│ 👤 Você:                                                 │
│ [Digite sua próxima pergunta________________]           │
│                                            [ Enviar ]   │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

**Características do Chat**:
1. **Context Bar** sempre visível no topo
2. **Sources** clicáveis com preview inline
3. **Confidence score** visível
4. **Disclaimer** em cada resposta
5. **Typing indicator** durante geração
6. **Copy button** para copiar resposta
7. **Export conversation** (PDF/TXT)
8. **Keyboard shortcuts**: Enter para enviar, Shift+Enter para nova linha

### 5. **Detalhes do Processo (`processo-detalhe.html?id=X`)**

**Layout**:
```
┌─────────────────────────────────────────────────────────┐
│ Navbar                                                   │
├──────────┬──────────────────────────────────────────────┤
│          │ 📂 PROCESSO 0001234-56.2023.5.02.0001         │
│          │                                              │
│ MENU     │ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│          │                                              │
│ Resumo   │ IDENTIFICAÇÃO                                │
│ Timeline │ Número: 0001234-56.2023.5.02.0001            │
│ Docs     │ Tipo: Trabalhista | Foro: TRT-2 São Paulo   │
│ Partes   │ Autor: Maria Silva                           │
│ Prazos   │ Réu: Empresa XYZ Ltda                        │
│ Riscos   │ Valor: R$ 250.000,00                         │
│ Ações    │ Status: Em andamento                         │
│          │ Risco: 🔴 Alto (Score: 75/100)               │
│ [Export] │                                              │
│          │ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ │
│          │                                              │
│          │ TIMELINE (Últimas movimentações)             │
│          │ ┌────────────────────────────────────────┐  │
│          │ │ 🔵 16/10/2025 - Despacho               │  │
│          │ │    Prazo para manifestação             │  │
│          │ │    [Ver documento]                     │  │
│          │ ├────────────────────────────────────────┤  │
│          │ │ 🔵 15/10/2025 - Contestação juntada    │  │
│          │ │    Ré apresentou defesa               │  │
│          │ │    [Ver documento]                     │  │
│          │ ├────────────────────────────────────────┤  │
│          │ │ 🔵 10/09/2025 - Petição inicial        │  │
│          │ │    Processo iniciado                   │  │
│          │ │    [Ver documento]                     │  │
│          │ └────────────────────────────────────────┘  │
│          │                                              │
│          │ PRÓXIMOS PRAZOS                              │
│          │ ⏰ 30/10/2025 (3 dias) - Manifestação       │
│          │ ⏰ 15/11/2025 (18 dias) - Audiência         │
│          │                                              │
│          │ ANÁLISE DE RISCO                             │
│          │ • Valor elevado (+30 pontos)                 │
│          │ • Jurisprudência desfavorável (+25)          │
│          │ • Prazo crítico (+20)                        │
│          │                                              │
│          │ RECOMENDAÇÕES                                │
│          │ • Provisionar R$ 180.000                     │
│          │ • Considerar proposta de acordo              │
│          │ • Priorizar manifestação                     │
│          │                                              │
└──────────┴──────────────────────────────────────────────┘
```

### 6. **Relatórios (`relatorios.html`)**

**Templates prontos**:
1. **Resumo Executivo** (1 processo)
2. **Exposição Total** (todos os processos)
3. **Prazos da Semana**
4. **Processos Críticos** (top 10)
5. **Análise de Risco** (customizável)
6. **Precedentes Similares**

**Geração**:
- Formulário com parâmetros
- Preview antes de exportar
- Export: PDF, Word, Markdown
- Salvar templates customizados

### 7. **Configurações (`configuracoes.html`)**

**Seções**:
1. **Perfil do Usuário**
2. **Configurações do Tenant**
   - Disclaimer jurídico customizável
   - Modo conservador (on/off)
   - Lista branca de tribunais
3. **Integrações**
   - Google Drive (conectar/desconectar)
   - Email para alertas
4. **Segurança**
   - Alterar senha
   - 2FA
   - Audit log (visualizar)

---

## 🔧 COMPONENTES REUTILIZÁVEIS

### 1. **ProcessoCard** (Card de processo)

```html
<div class="processo-card" data-processo-id="123">
  <div class="card shadow-sm border-start border-5 border-danger">
    <div class="card-body">
      <div class="d-flex justify-content-between align-items-start">
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
            <li><a class="dropdown-item" href="/processo-detalhe.html?id=123">Ver detalhes</a></li>
            <li><a class="dropdown-item" onclick="openChat('123')">Consultar IA</a></li>
            <li><a class="dropdown-item" onclick="exportProcesso('123')">Exportar</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</div>
```

### 2. **QuickActionButton** (Botão de ação rápida)

```html
<button class="quick-action-btn" data-action="resumo-executivo">
  <div class="quick-action-icon">
    <i class="bi bi-file-earmark-text fs-3"></i>
  </div>
  <div class="quick-action-label">
    Resumo Executivo
  </div>
</button>

<style>
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
  box-shadow: var(--lawflake-shadow);
  transform: translateY(-2px);
}

.quick-action-icon {
  color: var(--lawflake-primary);
  margin-bottom: 0.5rem;
}

.quick-action-label {
  font-weight: 600;
  color: var(--lawflake-text);
  font-size: 0.9rem;
}
</style>
```

### 3. **SourceCitation** (Citação de fonte)

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
    <button class="btn btn-sm btn-outline-primary" onclick="openDocument('doc_123', 3)">
      Abrir
    </button>
  </div>
</div>
```

### 4. **RiskBadge** (Badge de risco)

```html
<span class="badge risk-badge risk-alto">
  🔴 Alto Risco
</span>

<style>
.risk-badge {
  font-size: 0.85rem;
  padding: 0.4rem 0.8rem;
  font-weight: 600;
}

.risk-alto {
  background-color: #8b1a1a;
  color: white;
}

.risk-medio {
  background-color: #8b6914;
  color: white;
}

.risk-baixo {
  background-color: #2d5016;
  color: white;
}
</style>
```

---

## 🎭 ANIMAÇÕES E TRANSIÇÕES

```css
/* Transições suaves */
* {
  transition: border-color 0.15s ease, box-shadow 0.15s ease;
}

/* Hover cards */
.card:hover {
  box-shadow: var(--lawflake-shadow-lg);
  transform: translateY(-2px);
}

/* Loading spinner para ações de IA */
.ai-loading {
  animation: pulse 1.5s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* Typing indicator */
.typing-indicator span {
  animation: typing-dot 1.4s infinite;
}

.typing-indicator span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-indicator span:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes typing-dot {
  0%, 60%, 100% { opacity: 0.3; }
  30% { opacity: 1; }
}
```

---

## 🖥️ RESPONSIVIDADE

### Breakpoints

```css
/* Mobile-first approach */
--breakpoint-sm: 576px;
--breakpoint-md: 768px;
--breakpoint-lg: 992px;
--breakpoint-xl: 1200px;
--breakpoint-xxl: 1400px;

/* Desktop-first para LawFlake (maioria desktop) */
@media (max-width: 768px) {
  /* Sidebar vira accordion */
  /* Quick Actions viram lista vertical */
  /* Tabelas viram cards */
}
```

---

## 📂 ESTRUTURA DE ARQUIVOS

```
lawflake-frontend/
├── public/
│   ├── index.html  (Redirect para login)
│   ├── login.html
│   ├── dashboard.html
│   ├── processos.html
│   ├── processo-detalhe.html
│   ├── chat.html
│   ├── relatorios.html
│   ├── prazos.html
│   ├── perfil.html
│   ├── configuracoes.html
│   │
│   ├── assets/
│   │   ├── logo-lawflake.svg
│   │   ├── logo-lawflake-white.svg
│   │   ├── favicon.ico
│   │   └── images/
│   │
│   ├── css/
│   │   ├── lawflake.css  (Main styles)
│   │   ├── components.css  (Componentes reutilizáveis)
│   │   └── pages/
│   │       ├── dashboard.css
│   │       ├── chat.css
│   │       └── processos.css
│   │
│   ├── js/
│   │   ├── config.js  (API URLs, constants)
│   │   ├── auth.js  (Supabase auth)
│   │   ├── api.js  (API client)
│   │   ├── utils.js  (Helpers)
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
│   │       ├── chat.js
│   │       ├── processos.js
│   │       └── processo-detalhe.js
│   │
│   └── components/
│       ├── navbar.html  (Incluído em todas as páginas)
│       └── footer.html
│
├── vercel.json  (Vercel config)
├── package.json  (Se usar bundler - opcional)
└── README.md
```

---

## 🧪 PRIORIDADES DE IMPLEMENTAÇÃO

### **SPRINT 1 (3 dias): Foundation**

**Dia 1**:
- [ ] Setup: Vercel project, file structure
- [ ] CSS base: variables, typography, layout
- [ ] Componentes: navbar, footer
- [ ] Login page (auth Supabase)

**Dia 2**:
- [ ] Dashboard: layout + cards de estatísticas
- [ ] API client (api.js)
- [ ] Auth flow completo

**Dia 3**:
- [ ] Lista de processos (tabela + filtros básicos)
- [ ] ProcessoCard component
- [ ] Navegação entre páginas

### **SPRINT 2 (4 dias): Chat (PRIORIDADE MÁXIMA)**

**Dia 1-2**:
- [ ] Chat layout completo
- [ ] Context Bar component
- [ ] Seletor "Processo específico vs Todos"
- [ ] Quick Actions buttons (apenas UI)

**Dia 3**:
- [ ] Chat service integration
- [ ] Enviar mensagem + receber resposta
- [ ] Typing indicator
- [ ] Sources display

**Dia 4**:
- [ ] Quick Actions funcionais (chamadas API)
- [ ] Export conversation
- [ ] Polish UX (transições, loading states)

### **SPRINT 3 (2 dias): Detalhes e Relatórios**

**Dia 1**:
- [ ] Página de detalhes do processo
- [ ] Timeline component
- [ ] Análise de risco display

**Dia 2**:
- [ ] Página de relatórios
- [ ] Templates de relatório
- [ ] Export PDF/Word

### **SPRINT 4 (1 dia): Polish e Otimização**

- [ ] Responsividade mobile
- [ ] Animações e micro-interações
- [ ] Loading states e error handling
- [ ] Acessibilidade (ARIA labels)
- [ ] Performance (lazy loading)

---

## 🎯 DEFINIÇÃO DE PRONTO (DoD)

Cada página/componente está pronto quando:

- [ ] Layout implementado conforme mockup
- [ ] Responsivo (mobile + desktop)
- [ ] Conectado à API real (não mock)
- [ ] Loading states implementados
- [ ] Error handling implementado
- [ ] Acessível (keyboard navigation, ARIA)
- [ ] Testado em Chrome, Firefox, Safari
- [ ] Sem console errors

---

## 🚀 DEPLOY VERCEL

### `vercel.json`

```json
{
  "version": 2,
  "builds": [
    {
      "src": "public/**",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/public/$1"
    },
    {
      "src": "/",
      "dest": "/public/index.html"
    }
  ],
  "env": {
    "VITE_API_URL": "https://lawflake-backend.railway.app",
    "VITE_SUPABASE_URL": "@supabase_url",
    "VITE_SUPABASE_ANON_KEY": "@supabase_anon_key"
  }
}
```

### Deploy automático

- Conectar repo GitHub com Vercel
- Push para `main` → deploy automático
- Preview deployments para PRs

---

## 📚 BIBLIOTECAS E DEPENDÊNCIAS

**CSS/UI**:
- Bootstrap 5.3 (via CDN)
- Bootstrap Icons (via CDN)
- Google Fonts: Merriweather (serif), Inter (sans-serif)

**JS**:
- Supabase JS (via CDN) - Auth
- Chart.js (via CDN) - Gráficos
- Marked.js (via CDN) - Markdown rendering
- DOMPurify (via CDN) - XSS protection

**Opcional (se bundler)**:
- Vite (build tool)
- ESLint (linting)
- Prettier (formatting)

---

## 🎉 RESULTADO ESPERADO

Ao final da implementação, teremos:

✅ Interface profissional e séria para advogados
✅ Chat intuitivo com Quick Actions como protagonistas
✅ Sources sempre visíveis e clicáveis
✅ Dashboard com estatísticas críticas
✅ Lista de processos com filtros avançados
✅ Detalhes completos de cada processo
✅ Export de relatórios em PDF/Word
✅ Responsivo (desktop + mobile)
✅ Performance otimizada
✅ Acessível e testado

---

**Este frontend será o "rosto" do LawFlake. Cada pixel importa. 🏛️**
