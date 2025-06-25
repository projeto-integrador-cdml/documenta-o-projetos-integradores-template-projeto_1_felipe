[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/vZ6sAE2k)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19755600)

# Projeto Integrador I - Template Quarto

Este repositório é um modelo de documentação para o Projeto Integrador I dos cursos de Ciência de Dados e Machine Learning do CEUB. Ele está formatado segundo as normas da ABNT e estruturado com o sistema Quarto.

## 📄 Estrutura

- `index.qmd`: introdução geral
- `01-introducao.qmd`: contexto e objetivos
- `02-metodologia.qmd`: tecnologias, ferramentas e processos
- `03-desenvolvimento.qmd`: arquitetura, código e decisões
- `04-resultados.qmd`: imagens, gráficos, resultados
- `05-conclusao.qmd`: aprendizados e próximos passos
- `referencias.qmd`: lista de referências (com suporte `.bib`)
- `refs.bib`: arquivo BibTeX para citações
- `contracapa.tex`: contracapa em LaTeX para ABNT
- `imagens/`: coloque aqui capturas de tela e diagramas
- `_quarto.yml`: configurações do projeto

## 🚀 Como Usar

### Localmente (RStudio ou terminal)

1. Instale o Quarto: https://quarto.org/docs/get-started/
2. Certifique-se de que você possui LaTeX instalado (ex: [TinyTeX](https://yihui.org/tinytex/))
3. No terminal, rode:

```bash
quarto render
```

### Alternativa com GitHub Actions (renderização automática - opcional)

Será adicionado um arquivo `.github/workflows/render.yml` para gerar o PDF automaticamente a cada commit.

## 📌 Regras

- Documentação é obrigatória e será avaliada com base na completude e clareza.
- O código deve estar hospedado em repositório GitHub e ser referenciado neste relatório.

## 👨‍🏫 Suporte

Em caso de dúvidas, consulte os materiais no Moodle ou entre em contato com o professor responsável.


## 🧑‍💻 Boas Práticas de Programação

Para garantir a qualidade e a manutenção do código, é importante seguir algumas boas práticas. Aqui estão algumas diretrizes recomendadas:

### 1. **Nomes Significativos**
   - Use nomes claros e descritivos para variáveis, funções e métodos. Evite abreviações e nomes genéricos.
   
### 2. **Comentários Claros e Concisos**
   - Comente partes do código que sejam complexas ou pouco intuitivas. Evite comentários redundantes.
   - Utilize comentários de funções para descrever o que a função faz, seus parâmetros e o retorno.

### 3. **Evitar Código Repetido**
   - Siga o princípio DRY (Don't Repeat Yourself). Se identificar código repetido, extraia-o para funções ou métodos reutilizáveis.

### 4. **Organização do Código**
   - Organize o código em módulos e funções para manter a clareza e facilitar a manutenção.
   - Evite funções ou métodos grandes; prefira dividir a lógica em pequenas funções responsáveis por uma única tarefa.

### 5. **Consistência**
   - Mantenha um estilo de codificação consistente em todo o projeto (por exemplo, use PEP 8 para Python).
   - Use a mesma quantidade de espaços para indentação ao longo de todo o código.

### 6. **Tratamento de Erros**
   - Implemente tratamento de exceções de forma adequada para evitar falhas inesperadas.
   - As mensagens de erro devem ser claras e informativas.

### 7. **Testes**
   - Escreva testes unitários para validar a funcionalidade do seu código.
   - Use ferramentas de integração contínua para rodar os testes automaticamente com cada commit.
   - Garanta que o código crítico tenha boa cobertura de testes.

### 8. **Controle de Versão**
   - Utilize o Git para versionamento de código e siga práticas como commits pequenos e frequentes.
   - Utilize branches para implementar novas funcionalidades ou corrigir bugs sem afetar o código principal.

### 9. **Eficiência**
   - Escreva código eficiente e escolha estruturas de dados e algoritmos apropriados para melhorar o desempenho.
   - Utilize técnicas como lazy loading ou caching quando necessário.

### 10. **Documentação**
   - Documente seu código utilizando ferramentas como Javadoc (para Java) ou Sphinx (para Python).
   - Mantenha o README sempre atualizado com instruções claras de instalação, uso e contribuição.

