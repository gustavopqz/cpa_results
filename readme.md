# Aplicativo streamlit com resultados da pesquisa de satisfação CPA - UNEF e UNIFAN
## Linguagem utlizada: Python
## Leitura de arquivos: xlsx
## Dependencias:
- Python 3
- Streamlit
- Pandas
- Altair
- Codecs

## Estrutra xlsx UNEF
- Professor
    CURSO
    TURMA
    resp_teacher_name
    idpergunta
    quest_description
    INSUFICIENTE
    REGULAR
    BOM
    ÓTIMO
    EXCELENTE

- Coordenador
    COORDENADOR
    CURSO
    CODTURMA
    idpergunta
    Pergunta
    INSUFICIENTE
    REGULAR
    BOM
    ÓTIMO
    EXCELENTE

- Diretor
    CURSO
    idpergunta
    Pergunta
    INSUFICIENTE
    REGULAR
    BOM
    ÓTIMO
    EXECELENTE

- Sugestivas (professor e coordenador)
    NOME
    SUGESTIVAS

## Estrutra xlsx UNIFAN
- Professor
    CURSO
    TURMA
    resp_teacher_name
    idpergunta
    Pergunta
    INSUFICIENTE
    REGULAR
    BOM
    ÓTIMO
    EXCELENTE

- Coordenador
    COORDENADOR
    CURSO
    CODTURMA
    idpergunta
    Pergunta
    INSUFICIENTE
    REGULAR
    BOM
    ÓTIMO
    EXCELENTE

- Diretor
    CURSO
    idpergunta
    Pergunta
    INSUFICIENTE
    REGULAR
    BOM
    ÓTIMO
    EXECELENTE

- Sugestivas (professor e coordenador)
    NOME
    SUGESTIVAS

## Instância
Para instanciar o projeto é necessário rodar uma consulta no banco de dados da produção RM de cada instituição
Após a consulta os dados devem ser tratados para a forma que o xlsx aceita