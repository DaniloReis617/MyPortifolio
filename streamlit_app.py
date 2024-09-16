import streamlit as st

# Configuração da página
st.set_page_config(page_title="Danilo Reis - Portfólio", page_icon="./assets/logoCortado_free-file.png", layout="wide")

st.logo("./assets/dks_branco.png")

# Criação das abas principais
tab_inicio, tab_sobre, tab_projetos, tab_cursos, tab_contato = st.tabs(["🏠 Início", "👤 Sobre", "💼 Projetos", "📚 Cursos", "📧 Contato"])

# Estilo customizado para o layout
st.markdown("""
    <style>
        .btn {
            display: inline-block;
            padding: 0.75em 1.25em;
            font-size: 16px;
            font-weight: 600;
            text-align: center;
            color: #ffffff;
            background-color: #0e1117;
            border: none;
            border-radius: 25px;
            text-decoration: none;
        }
        .btn:hover {
            background-color: #28a745;
        }
        .section {
            margin-top: 40px;
        }
        .skills-bar {
            display: flex;
            justify-content: space-around;
        }
        .skill {
            width: 200px;
            text-align: center;
        }
        .skill-bar {
            background-color: #eee;
            border-radius: 25px;
        }
        .skill-level {
            background-color: #28a745;
            height: 25px;
            border-radius: 25px;
        }
    </style>
""", unsafe_allow_html=True)

# Conteúdo da aba "Início"
with tab_inicio:
    st.markdown("""
        <div style="text-align: center;">
            <h1>Olá, eu sou Danilo Reis</h1>
            <h3>Engenheiro de Dados, RPA e Desenvolvedor de Sistemas</h3>
            <p>Automação de processos com ferramentas como Power Automate, bots e scripts que otimizam tarefas repetitivas.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="padding:20px;border-radius:10px;margin-bottom:20px;">
            <h3>Projetos de Automação RPA</h3>
            <p>Automação de processos com ferramentas como Power Automate, bots e scripts que otimizam tarefas repetitivas.</p>
        </div>
        <div style="padding:20px;border-radius:10px;margin-bottom:20px;">
            <h3>Desenvolvimento de Sistemas</h3>
            <p>Desenvolvimento de soluções personalizadas em Python e VBA, integrando diferentes sistemas para uma automação completa.</p>
        </div>
        <div style="padding:20px;border-radius:10px;margin-bottom:20px;">
            <h3>Inteligência Artificial</h3>
            <p>Explorando modelos de Machine Learning e soluções baseadas em IA para otimização de processos e análise de dados.</p>
        </div>
        <div style="padding:20px;border-radius:10px;margin-bottom:20px;">
            <h3>Criptomoedas e Blockchain</h3>
            <p>Análise de criptomoedas e desenvolvimento de scripts para automatizar monitoramento e transações.</p>
        </div>
        <div style="padding:20px;border-radius:10px;margin-bottom:20px;">
            <h3>Estoicismo na Programação</h3>
            <p>Aplicando os princípios do estoicismo para manter o foco e a disciplina, gerando resiliência diante dos desafios de programação.</p>
        </div>
    """, unsafe_allow_html=True)

# Conteúdo da aba "Sobre"
with tab_sobre:
    st.header("Sobre Mim")
    st.write("""
    Sou um engenheiro de dados apaixonado por tecnologia e automação, com experiência em Python, SQL, VBA e Power BI. 
    Atualmente, trabalho com automação de processos (RPA), desenvolvimento de soluções de software e criação de pipelines de dados.
    """)
    st.header("Habilidades")
    st.markdown("""
    <div class="skills-bar">
        <div class="skill">
            <h4>Python</h4>
            <div class="skill-bar">
                <div class="skill-level" style="width: 90%;"></div>
            </div>
        </div>
        <div class="skill">
            <h4>SQL</h4>
            <div class="skill-bar">
                <div class="skill-level" style="width: 80%;"></div>
            </div>
        </div>
        <div class="skill">
            <h4>Power BI</h4>
            <div class="skill-bar">
                <div class="skill-level" style="width: 75%;"></div>
            </div>
        </div>
        <div class="skill">
            <h4>R</h4>
            <div class="skill-bar">
                <div class="skill-level" style="width: 85%;"></div>
            </div>
        </div>
        <div class="skill">
            <h4>Dax</h4>
            <div class="skill-bar">
                <div class="skill-level" style="width: 70%;"></div>
            </div>
        </div>
        <div class="skill">
            <h4>JavaScript</h4>
            <div class="skill-bar">
                <div class="skill-level" style="width: 70%;"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.header("Experiência")
    st.markdown("""
    <ul>
        <li><strong>Time Now (Atual)</strong>: Desenvolvedor RPA - Automação de Processos, ETL, Metodologias Ágeis e Scrum, Programação em Python, VBA e Power Apps, RPA, Bancos de Dados e SQL, Análise de Dados, Gerenciamento de Automações.</li>
        <li><strong>BRF S.A. (2021 - 2022)</strong>: Auxiliar Administrativo de Faturamento - Gestão de Frotas e Telecom, Automação de Processos, Metodologias Ágeis, Ferramentas Microsoft, SAP, Power BI, Excel, Power Apps, SharePoint, One Drive.</li>
    </ul>
    """, unsafe_allow_html=True)

    st.header("Educação")
    st.markdown("""
    <ul>
        <li>MBA em Gestão Estratégica de Projetos - UNIFACS (Abril 2025)</li>
        <li>Bacharel em Administração - Universidade Estadual da Bahia (Trancado)</li>
        <li>Tecnólogo em Gestão Pública - Centro Universitário Estácio (Concluído - 2022)</li>
        <li>Tecnólogo em Gestão de Tecnologia da Informação - Centro Universitário Estácio (Setembro 2024)</li>
    </ul>
    """, unsafe_allow_html=True)

    st.header("Outras Competências")
    st.markdown("""
    <ul>
        <li>Capacidade de analisar informações técnicas complexas</li>
        <li>Análise, projeção, mapeamento e implementação de KPI's</li>
        <li>Atencioso, detalhista, organizado e focado no Just Time</li>
        <li>Capacidade de solucionar conflitos, aprendizagem rápida e dinamismo</li>
    </ul>
    """, unsafe_allow_html=True)
    # Rodapé
    st.markdown("""
    <hr>
    <p style="text-align: center;">© 2024 Danilo Reis - Todos os direitos reservados</p>
    """, unsafe_allow_html=True)

# Conteúdo da aba "Projetos"
with tab_projetos:

    st.header("Meus Projetos")

    # Estilos CSS
    st.markdown("""
        <style>
            .btn {
                display: inline-block;
                padding: 10px 20px;
                margin-top: 10px;
                border-radius: 5px;
                background-color: #007bff;
                color: white;
                text-decoration: none;
                transition: background-color 0.3s;
            }
            .btn:hover {
                background-color: #0056b3;
            }
        </style>
    """, unsafe_allow_html=True)

    # Conteúdo dos projetos
    projects = [
        {
            "title": "Dashboard de Acompanhamento de Ações",
            "image": "assets/Power BI.png",
            "description": "Objetivo: Criar um dashboard interativo em Power BI para monitorar o desempenho de ações, facilitando a análise e a tomada de decisões de investimento.\n\nDescrição:\n- Coleta de Dados: Importação de dados históricos e em tempo real de preços de ações.\n- Transformação de Dados: Limpeza e preparação dos dados para análise.\n- Visualizações: Desenvolvimento de gráficos e tabelas interativas para acompanhar o desempenho das ações.\n- Análises Avançadas: Implementação de análises preditivas e alertas para mudanças significativas.\n- Compartilhamento: Publicação do dashboard para acesso online e colaboração.\n\nBenefícios: Melhor tomada de decisões de investimento, análise eficiente de dados financeiros e fácil acesso às informações.",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiZTQyZTE1ODYtZGQ0MS00OTFkLTkwODktYmQyODY3MzkyZWViIiwidCI6IjlhNzU5NGVjLWMxODUtNDIxYS04MmUxLTJlNWJkNDhiZmE3NSJ9"
        },
        {
            "title": "Projeto 2",
            "image": "assets/Power Apps.png",
            "description": "Descrição breve do projeto.",
            "link": "https://app.powerbi.com/view?r=eyJrIjoiZTQyZTE1ODYtZGQ0MS00OTFkLTkwODktYmQyODY3MzkyZWViIiwidCI6IjlhNzU5NGVjLWMxODUtNDIxYS04MmUxLTJlNWJkNDhiZmE3NSJ9"
        },
        {
            "title": "Projeto 3",
            "image": "assets/streamlit-logo.png",
            "description": "Descrição breve do projeto.",
            "link": "https://github.com/DaniloReis617"
        },
        {
            "title": "Projeto 4",
            "image": "assets/Python.jpeg",
            "description": "Descrição breve do projeto.",
            "link": "https://github.com/DaniloReis617"
        }
    ]

    # Renderização dos projetos
    with st.container():
        cols = st.columns(4)
        for i, project in enumerate(projects):
            with cols[i % 4]:
                st.image(project['image'], width=200)
                st.markdown(f"### {project['title']}")
                st.markdown(f"{project['description']}")
                st.link_button(f"Ver {project['title']}.", project['link'], type="secondary")

# Conteúdo da aba "Cursos" com sub-abas
with tab_cursos:
    st.header("Cursos")
    
    # Sub-abas dentro de "Cursos"
    sub_tab_powerbi, sub_tab_outros = st.tabs(["Power BI", "Outros Cursos"])

    # Sub-aba "Power BI"
    with sub_tab_powerbi:
        st.header("Domine o Power BI: Guia Completo para Análise de Dados e Business Intelligence")

        st.markdown("""
        ### Introdução
        - **Apresentação do Power BI**: Uma breve introdução sobre o que é o Power BI, sua importância no mercado de BI e análise de dados.
        - **Importância da Análise de Dados**: Explicação sobre como a análise de dados pode transformar negócios e ajudar na tomada de decisões.
        - **Objetivos do E-book**: O que os leitores podem esperar aprender e alcançar ao ler o e-book.

        ### Capítulo 1: Introdução ao Power BI
        - **O que é Power BI?**: Definição e visão geral do Power BI, incluindo seus componentes principais.
        - **Componentes do Power BI**:
            - Power BI Desktop: Ferramenta de criação de relatórios.
            - Power BI Service: Plataforma online para publicação e compartilhamento de relatórios.
            - Power BI Mobile: Aplicativo para visualização de relatórios em dispositivos móveis.
        - **Instalação e Configuração Inicial**: Passo a passo para baixar, instalar e configurar o Power BI Desktop.

        ### Capítulo 2: Conectando e Transformando Dados
        - **Conectando-se a Diferentes Fontes de Dados**:
            - Excel: Como importar dados de planilhas Excel.
            - SQL Server: Conexão com bancos de dados SQL Server.
            - Web: Importação de dados de fontes online.
        - **Usando o Power Query para Transformar Dados**:
            - Limpeza de Dados: Remoção de duplicatas, tratamento de valores nulos, etc.
            - Transformações Comuns: Alteração de tipos de dados, divisão de colunas, mesclagem de tabelas.
            - Limpeza e Preparação de Dados: Técnicas para garantir que os dados estejam prontos para análise.

        ### Capítulo 3: Modelagem de Dados
        - **Criação de Relacionamentos entre Tabelas**: Como conectar tabelas diferentes para criar um modelo de dados robusto.
        - **Uso de DAX (Data Analysis Expressions)**:
            - Medidas: Criação de cálculos dinâmicos.
            - Colunas Calculadas: Adição de colunas com base em fórmulas.
        - **Boas Práticas de Modelagem de Dados**: Dicas para manter um modelo de dados eficiente e fácil de manter.

        ### Capítulo 4: Visualizações e Relatórios
        - **Importação e Transformação de Dados**:
            - Como obter dados, transformá-los e preparar para visualizações.
        - **Criação de Relacionamentos e Medidas**:
            - Usando DAX para criar cálculos dinâmicos e conectando tabelas.
        - **Criação de Visualizações**: Adicionando gráficos, mapas e tabelas aos relatórios.
        - **Personalização de Visualizações**: Ajuste de cores, formatação de eixos, rótulos de dados, etc.
        - **Filtros e Slicers**: Adicionando filtros interativos.

        ### Capítulo 5: Dashboards Interativos
        - **Diferença entre Relatórios e Dashboards**: Explicação sobre as características e usos de cada um.
        - **Criação e Compartilhamento de Dashboards**: Como combinar visualizações em um dashboard e compartilhá-lo com outros usuários.
        - **Uso de Filtros e Slicers para Interatividade**: Adição de elementos interativos para permitir que os usuários explorem os dados.

        ### Capítulo 6: Publicação e Compartilhamento
        - **Publicação de Relatórios no Power BI Service**: Passo a passo para publicar relatórios online.
        - **Compartilhamento de Relatórios e Dashboards**: Como compartilhar seu trabalho com colegas e clientes.
        - **Configuração de Permissões e Segurança**: Controle de acesso e segurança dos dados.

        ### Capítulo 7: Power BI e Inteligência Artificial
        - **Uso de Recursos de IA no Power BI**:
            - Q&A: Ferramenta de perguntas e respostas baseada em IA.
            - Insights: Sugestões automáticas de insights baseados nos dados.
            - Integração com Azure Machine Learning: Como conectar modelos de machine learning ao Power BI.
        - **Exemplos Práticos de Uso de IA em Relatórios**: Casos de uso e exemplos de como a IA pode melhorar a análise de dados.

        ### Capítulo 8: Casos de Uso e Exemplos Práticos
        - **Estudos de Caso de Diferentes Indústrias**:
            - Financeira: Análise de desempenho financeiro.
            - Saúde: Monitoramento de indicadores de saúde.
            - Varejo: Análise de vendas e comportamento do consumidor.
        - **Exemplos de Relatórios e Dashboards Reais**: Demonstrações de relatórios e dashboards utilizados em situações reais.
        - **Dicas e Truques para Otimizar o Uso do Power BI**: Sugestões para melhorar a eficiência e eficácia no uso do Power BI.

        ### Conclusão
        - **Resumo dos Pontos Principais**: Recapitulação dos principais aprendizados do e-book.
        - **Próximos Passos para Continuar Aprendendo**: Recomendações de recursos adicionais e cursos para aprofundar o conhecimento.
        - **Recursos Adicionais e Leituras Recomendadas**: Links para tutoriais, blogs, e livros sobre Power BI.
        """)

    # Sub-aba "Outros Cursos" (pode ser preenchida posteriormente)
    with sub_tab_outros:
        st.header("Outros Cursos")
        st.write("Aqui você pode adicionar outros cursos relevantes.")
        
# Conteúdo da aba "Contato"
with tab_contato:
    st.header("Contato")
    
    # Formulário de contato expansível
    with st.popover("Formulário de Contato",use_container_width=True):
        with st.form(key='contact_form'):
            st.header("Preencher Dados:")
            nome = st.text_input("Nome")
            email = st.text_input("E-mail")
            mensagem = st.text_area("Mensagem")
            submit_button = st.form_submit_button(label="Enviar")

            if submit_button:
                st.success("Sua mensagem foi enviada com sucesso!")

    # Inclua o link para o CSS do Font Awesome
    st.markdown("""
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    """, unsafe_allow_html=True)

    # Adicione os ícones das redes sociais e o link do WhatsApp
    st.markdown("""
        <div style="display: flex; justify-content: space-around;">
            <a href="https://api.whatsapp.com/send?phone=5571993443078" target="_blank"><i class="fab fa-whatsapp"></i> WhatsApp</a>
            <a href="https://www.linkedin.com/in/daniloreis2196/" target="_blank"><i class="fab fa-linkedin"></i> LinkedIn</a>
            <a href="https://github.com/DaniloReis617" target="_blank"><i class="fab fa-github"></i> GitHub</a>
            <a href="https://www.instagram.com/danilo.reis_dev/" target="_blank"><i class="fab fa-instagram"></i> Instagram</a>
        </div>
    """, unsafe_allow_html=True)

