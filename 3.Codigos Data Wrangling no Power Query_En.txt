# PESQUISA CMA - 2025

### Em língua inglesa
**Respondidada entre:**  12/06/2025 a 29/09/2025

## CÓDIGOS DE DATA WRANGLING

### ID















### DESAFIOS ENFRENTADOS
**What types of changes do you typically manage? (Select all that apply) 
>>> Mudei o nome da coluna para ["col_work"], para facilitar a codificação abaixo e finalizando o tratamento da coluna 
retornarei o nome original.
========================================================================================================================
> Substituo as vírgulas do conteúdo das respostas para posteriormente separar as possíveis 3 maoires dificuldades
3Deseafios =
if Text.Contains([col_work],"tempo,",Comparer.OrdinalIgnoreCase) or 
   Text.Contains([col_work],"orçamento,",Comparer.OrdinalIgnoreCase) then 
   Text.Replace([col_work], "o,", "o;")
else 
if Text.Contains([col_work],"Outro",Comparer.OrdinalIgnoreCase) then 
   Text.Replace([col_work], "o:", "o")
else
  [col_work]

> Separação dos 3 desafios indicado na coluna [col_work] para as colunas [Desafio1], [Desafio2], [Desafio3]
Desafio1 = Text.Trim(Text.BeforeDelimiter([col_work], ",")) 
Desafio_W = Text.Trim(Text.AfterDelimiter([col_work], ",")) 
Desafio2 = Text.Trim(Text.BeforeDelimiter([Desafio_W], ","))
Desafio3 = Text.Trim(Text.AfterDelimiter([Desafio_W], ","))

> Transformação das colunas em linhas
Selecionar a coluna ID e no Menu do Power Query "Transformar". "Trasnformar outras colunas em linhas"

> Agrupar pela coluna "Valor", remover a coluna ID e no Menu do Power Query "Página inicial", "Agrupar por" ao final
retornar o nome original


### TIPOS DE MUDANÇAS GERENCIADAS
**What types of changes do you typically manage? (Select all that apply) 
>>> Mudei o nome da coluna para ["col_work"], para facilitar a codificação abaixo e finalizando o tratamento da coluna 
retornarei o nome original.
========================================================================================================================
> Separação dos até 7 tipos de mudanças selecionáveis
Tipo1 = 
if Text.Contains([col_work],"Technology Implementations",Comparer.OrdinalIgnoreCase) then 
   "Technology Implementations"
else ""

Tipo2 = 
if Text.Contains([col_work],"Organizational Restructuring",Comparer.OrdinalIgnoreCase) then 
   "Organizational Restructuring"
else ""

Tipo3 = 
if Text.Contains([col_work],"Process Improvements",Comparer.OrdinalIgnoreCase) then 
   "Process Improvements"
else ""

Tipo4 = 
if Text.Contains([col_work],"Cultural Change",Comparer.OrdinalIgnoreCase) then 
   "Cultural Change"
else ""

Tipo5 = 
if Text.Contains([col_work],"Policy or Regulatory Change",Comparer.OrdinalIgnoreCase) then 
   "Policy or Regulatory Change"
else ""

Tipo6 = 
if Text.Contains([col_work],"M&A Integration",Comparer.OrdinalIgnoreCase) then 
   "M&A Integration"
else ""

> Transformação das colunas em linhas
Selecionar a coluna ID e no Menu do Power Query "Transformar". "Trasnformar outras colunas em linhas"

> Agrupar pela coluna "Valor", remover a coluna ID e no Menu do Power Query "Página inicial", "Agrupar por" ao final
retornar o nome original



### METODOLOGIA DE GMO
**Which Change Management methodologies do you primarily use? ( Select up to 3 options) 
>>> Mudei o nome da coluna para ["col_work"], para facilitar a codificação abaixo e finalizando o tratamento da coluna 
retornarei o nome original.
========================================================================================================================
> Separação das 3 metodologias possíveis indicadas na coluna [col_work] para as colunas [Metodologia1], [Metodologia2], [Metodologia3]
metod1 = Text.Trim(Text.BeforeDelimiter([col_work], ",")) 
metod_W = Text.Trim(Text.AfterDelimiter([col_work], ",")) 
metod2 = Text.Trim(Text.BeforeDelimiter([metod_W], ","))
metod3 = Text.Trim(Text.AfterDelimiter([metod_W], ","))

> Transformação das colunas em linhas
Selecionar a coluna ID e no Menu do Power Query "Transformar". "Trasnformar outras colunas em linhas"

> Agrupar pela coluna "Valor", remover a coluna ID e no Menu do Power Query "Página inicial", "Agrupar por" ao final
retornar o nome original


### FERRAMENTAS UTILIZADAS	
**Which tools are commonly used in your OCM practice? ( Select all that apply)
>>> Renomeei a coluna ["Quais ferramentas são comumente utilizadas em sua prática de GMO? (Selecione todas as opções aplicáveis)
 para ["col_work"] para facilitar a codificação abaixo e só depois do fim de todo tratamento 
retornarei o nome original.
========================================================================================================================
> Separação dos até 14 tipos de ferramentas
Tool1 = 
if Text.Contains([col_work],"Stakeholder Mapping Tools",Comparer.OrdinalIgnoreCase) then 
   "Stakeholder Mapping Tools"
else ""

Tool2 = 
if Text.Contains([col_work],"Influence Networks Design",Comparer.OrdinalIgnoreCase) then 
   "Influence Networks Design"
else ""

Tool3 = 
if Text.Contains([col_work],"Assessment of Organizational Culture",Comparer.OrdinalIgnoreCase) then 
   "Assessment of Organizational Culture"
else ""

Tool4 = 
if Text.Contains([col_work],"Change Impact Assessment",Comparer.OrdinalIgnoreCase) then 
   "Change Impact Assessment"
else ""

Tool5 = 
if Text.Contains([col_work],"Communication Planning Tools",Comparer.OrdinalIgnoreCase) then 
   "Communication Planning Tools"
else ""

Tool6 = 
if Text.Contains([col_work],"Training Planning and Management Tools",Comparer.OrdinalIgnoreCase) then 
   "Training Planning and Management Tools"
else ""

Tool7 = 
if Text.Contains([col_work],"Indicators of Readiness for Change",Comparer.OrdinalIgnoreCase) then 
   "Indicators of Readiness for Change"
else ""

Tool8 = 
if Text.Contains([col_work],"Indicators of Change Assimilation",Comparer.OrdinalIgnoreCase) then 
   "Indicators of Change Assimilation"
else ""

Tool9 = 
if Text.Contains([col_work],"Dashboards / Análises de GM",Comparer.OrdinalIgnoreCase) then 
   "CM Dashboards / Analytics"
else ""

Tool10 = 
if Text.Contains([col_work],"Employee Feedback Systems",Comparer.OrdinalIgnoreCase) then 
   "Employee Feedback Systems"
else ""

Tool11 = 
if Text.Contains([col_work],"Risk Map",Comparer.OrdinalIgnoreCase) then 
   "Risk Map"
else ""

Tool12 = 
if Text.Contains([col_work],"Lessons Learned Map",Comparer.OrdinalIgnoreCase) then 
   "Lessons Learned Map"
else ""

Tool13 = 
if Text.Contains([col_work],"3D Stakeholder Management",Comparer.OrdinalIgnoreCase) then 
   "3D Stakeholder Management"
else ""

Tool14 = 
if Text.Contains([col_work],"None",Comparer.OrdinalIgnoreCase) then 
   "None"
else ""

> Transformação das colunas em linhas
Selecionar a coluna ID e no Menu do Power Query "Transformar". "Trasnformar outras colunas em linhas"

> Agrupar pela coluna "Valor", remover a coluna ID e no Menu do Power Query "Página inicial", "Agrupar por" ao final
retornar o nome original


### FAMILIARIDADE COM O SOFTWARE	
**What Change Management software/apps are you familiar with? (Select all that apply)  
>>> Renomeei a coluna ["Com quais softwares/aplicativos de Gestão de Mudanças você está familiarizado?
 para ["col_work"] para facilitar a codificação abaixo e só depois do fim de todo tratamento 
retornarei o nome original.
========================================================================================================================
> Separação dos até 9 softwares familiarizado
SW1 = 
if Text.Contains([col_work],"HCMBOK TOOLS (by HUCMI)",Comparer.OrdinalIgnoreCase) then 
   "HCMBOK TOOLS (by HUCMI)"
else ""

SW2 = 
if Text.Contains([col_work],"Change Hub",Comparer.OrdinalIgnoreCase) then 
   "Change Hub"
else ""

SW3 = 
if Text.Contains([col_work],"The Change Compass",Comparer.OrdinalIgnoreCase) then 
   "The Change Compass"
else ""

SW4 = 
if Text.Contains([col_work],"Prosci Change Management Platform",Comparer.OrdinalIgnoreCase) then 
   "Prosci Change Management Platform"
else ""

SW5 = 
if Text.Contains([col_work],"ADKAR Dashboard",Comparer.OrdinalIgnoreCase) then 
   "ADKAR Dashboard"
else ""

SW6 = 
if Text.Contains([col_work],"OrgMapper",Comparer.OrdinalIgnoreCase) then 
   "OrgMapper"
else ""

SW7 = 
if Text.Contains([col_work],"Templates and Spreadsheets",Comparer.OrdinalIgnoreCase) then 
   "Templates and Spreadsheets"
else ""

SW8 = 
if Text.Contains([col_work],"None",Comparer.OrdinalIgnoreCase) then 
   "None"
else ""

SW9 = 
if (Text.Contains([col_work],"SAP",Comparer.OrdinalIgnoreCase) or 
    Text.Contains([col_work],"HP",Comparer.OrdinalIgnoreCase)) then 
   "Outro"
else ""

> Transformação das colunas em linhas
Selecionar a coluna ID e no Menu do Power Query "Transformar". "Trasnformar outras colunas em linhas"

> Agrupar pela coluna "Valor", remover a coluna ID e no Menu do Power Query "Página inicial", "Agrupar por" ao final
retornar o nome original



### SOFTWARE UTILIZOU	
**Which Change Management software/apps are you have used? (Select all that apply)  
>>> Renomeei a coluna ["Quais softwares/aplicativos de Gestão de Mudanças você já utilizou? (Selecione todas as opções aplicáveis)]
 para ["col_work"] para facilitar a codificação abaixo e só depois do fim de todo tratamento 
retornarei o nome original.
========================================================================================================================
> Separação dos até 9 softwares que utilizou
SW1 = 
if Text.Contains([col_work],"HCMBOK TOOLS (by HUCMI)",Comparer.OrdinalIgnoreCase) then 
   "HCMBOK TOOLS (by HUCMI)"
else ""

SW2 = 
if Text.Contains([col_work],"Change Hub",Comparer.OrdinalIgnoreCase) then 
   "Change Hub"
else ""

SW3 = 
if Text.Contains([col_work],"The Change Compass",Comparer.OrdinalIgnoreCase) then 
   "The Change Compass"
else ""

SW4 = 
if Text.Contains([col_work],"Prosci Change Management Platform",Comparer.OrdinalIgnoreCase) then 
   "Prosci Change Management Platform"
else ""

SW5 = 
if Text.Contains([col_work],"ADKAR Dashboard",Comparer.OrdinalIgnoreCase) then 
   "ADKAR Dashboard"
else ""

SW6 = 
if Text.Contains([col_work],"OrgMapper",Comparer.OrdinalIgnoreCase) then 
   "OrgMapper"
else ""

SW7 = 
if Text.Contains([col_work],"Templates and Spreadsheets",Comparer.OrdinalIgnoreCase) then 
   "Templates and Spreadsheets"
else ""

SW8 = 
if Text.Contains([col_work],"None",Comparer.OrdinalIgnoreCase) then 
   "None"
else ""

SW9 = 
if (Text.Contains([col_work],"SAP",Comparer.OrdinalIgnoreCase) or 
    Text.Contains([col_work],"HP",Comparer.OrdinalIgnoreCase)) then 
   "Outro"
else ""
> Transformação das colunas em linhas
Selecionar a coluna ID e no Menu do Power Query "Transformar". "Trasnformar outras colunas em linhas"

> Agrupar pela coluna "Valor", remover a coluna ID e no Menu do Power Query "Página inicial", "Agrupar por" ao final
retornar o nome original


### ENGAJAMENTO TÍPICO	
**How are stakeholders typically engaged during change initiatives? (Select at least 1 option) (Selecione pelo menos 1 opção)  
>>> Renomeei a coluna ["Como os stakeholders são tipicamente engajados durante as iniciativas de mudança? (Selecione pelo menos 1 opção)]
 para ["col_work"] para facilitar a codificação abaixo e só depois do fim de todo tratamento 
retornarei o nome original.
========================================================================================================================
> Separação dos até 4 tipos de engajamento
ENG1 = 
if Text.Contains([col_work],"One-way communication (newsletters, memos)",Comparer.OrdinalIgnoreCase) then 
   "One-way communication (newsletters, memos)"
else ""

ENG2 = 
if Text.Contains([col_work],"Two-way dialogue (town halls, feedback loops)",Comparer.OrdinalIgnoreCase) then 
   "Two-way dialogue (town halls, feedback loops)"
else ""

ENG3 = 
if Text.Contains([col_work],"Co-creation and involvement in planning",Comparer.OrdinalIgnoreCase) then 
   "Co-creation and involvement in planning"
else ""

ENG4 = 
if Text.Contains([col_work],"Change network or ambassadors",Comparer.OrdinalIgnoreCase) then 
   "Change network or ambassadors"
else ""

> Transformação das colunas em linhas
Selecionar a coluna ID e no Menu do Power Query "Transformar". "Trasnformar outras colunas em linhas"

> Agrupar pela coluna "Valor", remover a coluna ID e no Menu do Power Query "Página inicial", "Agrupar por" ao final
retornar o nome original


### TIPO DE INDICADORES
**What kind of indicators or tools do you use to assess change readiness? (Select at least 1 option)       
>>> Renomeei a coluna ["Que tipo de indicadores ou ferramentas você usa para avaliar a prontidão para a mudança? (Selecione pelo menos 1 opção)]
 para ["col_work"] para facilitar a codificação abaixo e só depois do fim de todo tratamento 
retornarei o nome original.
========================================================================================================================
> Separação dos até 7 indicadores
IND1 = 
if Text.Contains([col_work],"Change Readiness Surveys",Comparer.OrdinalIgnoreCase) then 
   "Change Readiness Surveys"
else ""

IND2 = 
if Text.Contains([col_work],"Stakeholder perception analysis",Comparer.OrdinalIgnoreCase) then 
   "Stakeholder perception analysis"
else ""

IND3 = 
if Text.Contains([col_work],"Leadership alignment assessments",Comparer.OrdinalIgnoreCase) then 
   "Leadership alignment assessments"
else ""

IND4 = 
if Text.Contains([col_work],"Communication effectiveness ratings",Comparer.OrdinalIgnoreCase) then 
   "Communication effectiveness ratings"
else ""

IND5 = 
if Text.Contains([col_work],"Training needs assessments",Comparer.OrdinalIgnoreCase) then 
   "Training needs assessments"
else ""

IND6 = 
if Text.Contains([col_work],"Team/department readiness workshops",Comparer.OrdinalIgnoreCase) then 
   "Team/department readiness workshops"
else ""

IND7 = 
if Text.Contains([col_work],"Resistance mapping",Comparer.OrdinalIgnoreCase) then 
   "Resistance mapping"
else ""

> Transformação das colunas em linhas
Selecionar a coluna ID e no Menu do Power Query "Transformar". "Trasnformar outras colunas em linhas"

> Agrupar pela coluna "Valor", remover a coluna ID e no Menu do Power Query "Página inicial", "Agrupar por" ao final
retornar o nome original


### METRICA DE SUCESSO
**How do you measure success in change initiatives?  (Select at least 1 option)       
>>> Renomeei a coluna ["Como você mede o sucesso em iniciativas de mudança?"]
 para ["col_work"] para facilitar a codificação abaixo e só depois do fim de todo tratamento 
retornarei o nome original.
========================================================================================================================
> Separação dos até 8 indicadores
METRICA1 = 
if Text.Contains([col_work],"Adoption metrics",Comparer.OrdinalIgnoreCase) then 
   "Adoption metrics"
else ""

METRICA2 = 
if Text.Contains([col_work],"Stakeholder engagement",Comparer.OrdinalIgnoreCase) then 
   "Stakeholder engagement"
else ""

METRICA3 = 
if Text.Contains([col_work],"Business performance KPIs",Comparer.OrdinalIgnoreCase) then 
   "Business performance KPIs"
else ""

METRICA4 = 
if Text.Contains([col_work],"OKRs (Objectives and Key Results)",Comparer.OrdinalIgnoreCase) then 
   "OKRs (Objectives and Key Results)"
else ""

METRICA5 = 
if Text.Contains([col_work],"Indicators of change assimilation",Comparer.OrdinalIgnoreCase) then 
   "Indicators of change assimilation"
else ""

METRICA6 = 
if Text.Contains([col_work],"Training outcomes (assessment results, practical application)",Comparer.OrdinalIgnoreCase) then 
   "Training outcomes (assessment results, practical application)"
else ""

METRICA7 = 
if Text.Contains([col_work],"Results from organizational climate or engagement surveys",Comparer.OrdinalIgnoreCase) then 
   "Results from organizational climate or engagement surveys"
else ""

METRICA8 = 
if Text.Contains([col_work],"Positive feedback from employees or stakeholders",Comparer.OrdinalIgnoreCase) then 
   "Positive feedback from employees or stakeholders"
else ""

> Transformação das colunas em linhas
Selecionar a coluna ID e no Menu do Power Query "Transformar". "Trasnformar outras colunas em linhas"

> Agrupar pela coluna "Valor", remover a coluna ID e no Menu do Power Query "Página inicial", "Agrupar por" ao final
retornar o nome original



### TIPO DE PROJETO
**What type of projects does your organization apply Change Management to? (Select a at least 1 option)       
>>> Renomeei a coluna ["Como você mede o sucesso em iniciativas de mudança? (Selecione pelo menos 1 opção)"]
 para ["col_work"] para facilitar a codificação abaixo e só depois do fim de todo tratamento 
retornarei o nome original.
========================================================================================================================
> Separação dos até 7 indicadores
PRJ1 = 
if Text.Contains([col_work],"Linear/Predictive",Comparer.OrdinalIgnoreCase) then 
   "Linear/Predictive"
else ""

PRJ2 = 
if Text.Contains([col_work],"Agile",Comparer.OrdinalIgnoreCase) then 
   "Agile"
else ""

PRJ3 = 
if Text.Contains([col_work],"Hybrid",Comparer.OrdinalIgnoreCase) then 
   "Hybrid"
else ""

PRJ4 = 
if Text.Contains([col_work],"None",Comparer.OrdinalIgnoreCase) then 
   "None"
else ""

PRJ5 = 
if Text.Contains([col_work],"Outro",Comparer.OrdinalIgnoreCase) then 
   "Outro"
else ""


> Transformação das colunas em linhas
Selecionar a coluna ID e no Menu do Power Query "Transformar". "Trasnformar outras colunas em linhas"

> Agrupar pela coluna "Valor", remover a coluna ID e no Menu do Power Query "Página inicial", "Agrupar por" ao final
retornar o nome original



### MAIOR DESAFIO
**What are the biggest challenge for organizational transformation of your organization for the next 2 years? (Select a at least 1 option) 
>>> Renomeei a coluna ["Qual é o maior desafio para a transformação organizacional da sua organização nos próximos 2 anos? (Selecione pelo menos 1 opção)"]
 para ["col_work"] para facilitar a codificação abaixo e só depois do fim de todo tratamento 
retornarei o nome original.
> Separação dos até 8 DESAFIOS
DESAFIO1 = 
if Text.Contains([col_work],"Lack of Change Management Knowledge",Comparer.OrdinalIgnoreCase) then 
   "Lack of Change Management Knowledge"
else ""

DESAFIO2 = 
if Text.Contains([col_work],"Lack of Change Management resources/budget",Comparer.OrdinalIgnoreCase) then 
   "Lack of Change Management resources/budget"
else ""

DESAFIO3 = 
if Text.Contains([col_work],"Lack of Change Leadership Knowledge",Comparer.OrdinalIgnoreCase) then 
   "Lack of Change Leadership Knowledge"
else ""

DESAFIO4 = 
if Text.Contains([col_work],"Lack of Change Leadership Protagonism",Comparer.OrdinalIgnoreCase) then 
   "Lack of Change Leadership Protagonism"
else ""

DESAFIO5 = 
if Text.Contains([col_work],"Lack of Change Management Tools",Comparer.OrdinalIgnoreCase) then 
   "Lack of Change Management Tools"
else ""

DESAFIO6 = 
if Text.Contains([col_work],"Poor integration between Project and Change Management",Comparer.OrdinalIgnoreCase) then 
   "Poor integration between Project and Change Management"
else ""

DESAFIO7 = 
if Text.Contains([col_work],"Poor integrations between Strategy execution and Change Management",Comparer.OrdinalIgnoreCase) then 
   "Poor integrations between Strategy execution and Change Management"
else ""

DESAFIO8 = 
if Text.Contains([col_work],"Poor Understanding of the importance of managing changes",Comparer.OrdinalIgnoreCase) then 
   "Poor Understanding of the importance of managing changes"
else ""

DESAFIO9 = 
if Text.Contains([col_work],"Change Fatigue/Saturation due to the amount of simultaneous changes",Comparer.OrdinalIgnoreCase) then 
   "Change Fatigue/Saturation due to the amount of simultaneous changes"
else ""

> Transformação das colunas em linhas
Selecionar a coluna ID e no Menu do Power Query "Transformar". "Trasnformar outras colunas em linhas"

> Agrupar pela coluna "Valor", remover a coluna ID e no Menu do Power Query "Página inicial", "Agrupar por" ao final
retornar o nome original



















##########################################################################################################################################



### CARGO AJUSTADO
>>> Cria a coluna ["Job adj"] a partir da condição abaixo
=====================================================================================================================================================
Job adj =
if (Text.Contains([#"Job Title:"],"Analist",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Aprendiz",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Changer",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Informaticicst",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Partner",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"planificación",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Senior",Comparer.OrdinalIgnoreCase) = true) then "Analist"
else 
if (Text.Contains([#"Job Title:"],"Consultor",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"adviser",Comparer.OrdinalIgnoreCase) or	
    Text.Contains([#"Job Title:"],"advisor",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"IMPROVEMENT",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Consultant",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Bewegingmaker",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Assessor",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Specialist",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Partner",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Expert",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Lecturer",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Engagement",Comparer.OrdinalIgnoreCase) or
	Text.Contains([#"Job Title:"],"Mentor",Comparer.OrdinalIgnoreCase) = true) then "Consultant"
else
if (Text.Contains([#"Job Title:"],"Lead",Comparer.OrdinalIgnoreCase) or 
    Text.Contains([#"Job Title:"],"Líder",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Coordenador",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Coordinator",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Supervisor",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Gestor",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Management",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Managenent",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"MD",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"PMO",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Manager",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Gerente",Comparer.OrdinalIgnoreCase) = true) then "Manager"
else
if (Text.Contains([#"Job Title:"],"Pesquisador",Comparer.OrdinalIgnoreCase) or 
    Text.Contains([#"Job Title:"],"Knowledge",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Researcher",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Student",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Estudante",Comparer.OrdinalIgnoreCase) = true) then "Researcher"
else 
if (Text.Contains([#"Job Title:"],"CIO",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Chief",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"CEO",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"CPO",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Head",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Principal",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Director",Comparer.OrdinalIgnoreCase) or
	Text.Contains([#"Job Title:"],"Diretor",Comparer.OrdinalIgnoreCase) = true) then "Director"
else 
if (Text.Contains([#"Job Title:"],"Entrepreneu",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Soci",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Founder",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"Owner",Comparer.OrdinalIgnoreCase) or
    Text.Contains([#"Job Title:"],"President",Comparer.OrdinalIgnoreCase) or
	Text.Contains([#"Job Title:"],"Empresario",Comparer.OrdinalIgnoreCase) = true) then "President"
else "N/A" 


### TAMANHO AJUSTADO
>> Renomeei a coluna ["Organization size (in number of employees)"] para ["col_work"] para facilitar o tratamento abaixo, 
criando a nova coluna ["Size adj"], depois retornei o  original
=====================================================================================================================================================
Size adj =
if Text.Contains([col_work],"Micro",Comparer.OrdinalIgnoreCase) then "a - Micro (1 - 09)"
else 
if Text.Contains([col_work],"Small",Comparer.OrdinalIgnoreCase) then "b - Small (10 - 49)"
else 
if Text.Contains([col_work],"Medium",Comparer.OrdinalIgnoreCase) then "c - Medium (50 - 249)"
else 
if Text.Contains([col_work],"Very",Comparer.OrdinalIgnoreCase) then "e - Very Large (1.000 a 4.999)"
else 
if Text.Contains([col_work],"Large",Comparer.OrdinalIgnoreCase) then "d - Large (250 - 999)"
else 
if Text.Contains([col_work],"Global",Comparer.OrdinalIgnoreCase) then "g - Global Enterprise (10.000 em diante)"
else 
if Text.Contains([col_work],"Enterprise",Comparer.OrdinalIgnoreCase) then "f - Enterprise (5.000 9.999)"
else "N/A"


### SENIORIDADE AJUSTADA
>>> Renomeei a coluna ["What is your current professional seniority level?"] para {"col_work"] para facilitar o tratamento abaixo, criando 
a nova coluna ["Seniority adj"], depois retornei o nome original
=====================================================================================================================================================
Seniority adj =
if Text.Contains([col_work],"Executive Leadership",Comparer.OrdinalIgnoreCase) then "Executive Leadership"
else 
if Text.Contains([col_work],"Mid-Level Management",Comparer.OrdinalIgnoreCase) then "Management"
else 
if Text.Contains([col_work],"Personal Operativo",Comparer.OrdinalIgnoreCase) then "Operational Staff"
else 
if Text.Contains([col_work],"Operational Staff",Comparer.OrdinalIgnoreCase) then "Operational Staff"
else 
if Text.Contains([col_work],"Consultant",Comparer.OrdinalIgnoreCase) then "Consultant"
else 
if Text.Contains([col_work],"governança",Comparer.OrdinalIgnoreCase) then "Outros"
else "N/A"


### PAPEL AJUSTADO
>>> Renomeei a coluna ["What is your current role in change management? (select the one that best fits your current role)"] para {"col_work"] para facilitar o tratamento abaixo, criando 
a nova coluna ["Role adj"], depois retornei o nome original
=====================================================================================================================================================
Role adj =
if Text.Contains([col_work],"Change",Comparer.OrdinalIgnoreCase) then "Condução da mudança"
else
if (Text.Contains([col_work],"Qyality",Comparer.OrdinalIgnoreCase) or
	Text.Contains([col_work],"Business",Comparer.OrdinalIgnoreCase) = true) then "Business Area"
else
if (Text.Contains([col_work],"CIO",Comparer.OrdinalIgnoreCase) or
	Text.Contains([col_work],"CTO",Comparer.OrdinalIgnoreCase) or
	Text.Contains([col_work],"C-level",Comparer.OrdinalIgnoreCase) or
	Text.Contains([col_work],"CEO",Comparer.OrdinalIgnoreCase) = true) then "Board"
else
if (Text.Contains([col_work],"Projeto",Comparer.OrdinalIgnoreCase) or
	Text.Contains([col_work],"Project",Comparer.OrdinalIgnoreCase) or
	Text.Contains([col_work],"PMO",Comparer.OrdinalIgnoreCase) = true) then "PMO"
else
if Text.Contains([col_work],"IT",Comparer.OrdinalIgnoreCase) then "IT Professional"
else
if Text.Contains([col_work],"Consultant",Comparer.OrdinalIgnoreCase) then "Consultant"
else
if Text.Contains([col_work],"Researcher",Comparer.OrdinalIgnoreCase) then "Other"
else
if Text.Contains([col_work],"Human",Comparer.OrdinalIgnoreCase) then "RH"
else "N/A" 


### VINCULAÇÃO AJUSTADA
>>> Renomeei a coluna ["Which area is the CMO or Change Management team/department linked to?"] para {"col_work"] para facilitar o tratamento abaixo, criando 
a nova coluna ["Vinculação ajustada"], depois retornei o nome original
=====================================================================================================================================================
Link adj =

if (Text.Contains([col_work],"RH",Comparer.OrdinalIgnoreCase) or
	Text.Contains([col_work],"People",Comparer.OrdinalIgnoreCase) = true) then "HR"
else
if (Text.Contains([col_work],"CTO",Comparer.OrdinalIgnoreCase) or
	Text.Contains([col_work],"CIO",Comparer.OrdinalIgnoreCase) = true) then "Digital Transformation"
else
if (Text.Contains([col_work],"Sales",Comparer.OrdinalIgnoreCase) or
    Text.Contains([col_work],"Segurança",Comparer.OrdinalIgnoreCase) or
    Text.Contains([col_work],"Consultoria",Comparer.OrdinalIgnoreCase) or
	Text.Contains([col_work],"específico",Comparer.OrdinalIgnoreCase) = true) then "Outros"
else [col_work]

   

### CONSISTÊNCIA DE ENGAJAMENTO
>>> Renomeei a coluna ["How consistently are stakeholder engagement activities conducted in your organization during change initiatives?"] para {"col_work"] para facilitar o tratamento abaixo, criando a nova coluna ["Atividades de engajamento"], depois retornei o nome original
=====================================================================================================================================================
Engage adj =
if Text.Contains([col_work],"Rarely –",Comparer.OrdinalIgnoreCase) then "Rarely"
else 
if Text.Contains([col_work],"Occasionally –",Comparer.OrdinalIgnoreCase) then "Occasionally"
else 
if Text.Contains([col_work],"Frequently –",Comparer.OrdinalIgnoreCase) then "Frequently"
else 
if Text.Contains([col_work],"Consistently –",Comparer.OrdinalIgnoreCase) then "Consistently"
else 
if Text.Contains([col_work],"Not sure",Comparer.OrdinalIgnoreCase) then "Not sure"
else "N/A"


### MATURIDADE DAS PRÁTICAS DE GMO
>>> Renomeei a coluna ["How mature would you classify Change Management practices in your company?"] 
para {"col_work"] para facilitar o tratamento abaixo, criando a nova coluna ["Maturidade das práticas em GMO"], 
depois retornei o nome original
========================================================================================================================
Mature GMO adj =
if Text.Contains([col_work],"Initial (",Comparer.OrdinalIgnoreCase) then "Initial"
else 
if Text.Contains([col_work],"Emerging (",Comparer.OrdinalIgnoreCase) then "Emergente"
else 
if Text.Contains([col_work],"Defined (",Comparer.OrdinalIgnoreCase) then "Defined"
else 
if Text.Contains([col_work],"Managed (",Comparer.OrdinalIgnoreCase) then "Managed"
else 
if Text.Contains([col_work],"Optimized (",Comparer.OrdinalIgnoreCase) then "Optimized"
else 
if Text.Contains([col_work],"Institutionalized (",Comparer.OrdinalIgnoreCase) then "Institutionalized"
else "N/A"



### MATURIDADE DA LIDERANÇA EM GMO
>>> Renomeei a coluna ["How mature is Change Leadership in your company?"] 
para {"col_work"] para facilitar o tratamento abaixo, criando a nova coluna ["Maturidade da liderança em GMO"], 
depois retornei o nome original
========================================================================================================================
Maturidade da liderança em GMO =
if Text.Contains([col_work],"Minimal (",Comparer.OrdinalIgnoreCase) then "Minimal"
else 
if Text.Contains([col_work],"Basic (",Comparer.OrdinalIgnoreCase) then "Basic"
else 
if Text.Contains([col_work],"Active (",Comparer.OrdinalIgnoreCase) then "Active"
else 
if Text.Contains([col_work],"Proactive (",Comparer.OrdinalIgnoreCase) then "Proactive"
else 
if Text.Contains([col_work],"Strategic (",Comparer.OrdinalIgnoreCase) then "Strategic"
else "N/A"



