# Carrinho de Compras: Qualidade e Teste

Implementação das regras de desconto progressivo, frete e validação do checkout para o trabalho prático de Qualidade e Teste de Software.

## Requisitos

- Python 3.10 ou superior
- Para executar os testes, nenhuma dependência externa é necessária.
- Para gerar o relatório PDF, instale ReportLab: `python -m pip install reportlab`.

## Executar os testes

Na pasta do projeto, execute:

```bash
python -m unittest -v test_carrinho
```

Os testes também podem ser iniciados diretamente com `python test_carrinho.py`.

## Gerar o relatório PDF

Depois de instalar ReportLab, execute:

```bash
python gerar_relatorio.py
```

O arquivo `relatorio_iso25010.pdf` será criado nesta pasta. O relatório inclui a análise ISO/IEC 25010, o mapeamento dos casos e a captura PNG do terminal na seção de evidência.

Para inserir a captura de tela do teste no PDF:

1. Execute `python -m unittest -v test_carrinho` no terminal.
2. Com o resultado `OK` visível, pressione `Win + Shift + S` e salve a captura como `captura_testes.png` nesta pasta do projeto.
3. Execute `python gerar_relatorio.py` novamente. O gerador inclui a imagem automaticamente no PDF.

## Arquivos

- `carrinho.py`: implementação da classe `CarrinhoDeCompras`.
- `test_carrinho.py`: testes unitários com `unittest`.
- `RELATORIO.md`: fonte textual do relatório.
- `gerar_relatorio.py`: gerador do PDF.
- `relatorio_iso25010.pdf`: relatório pronto para revisão e entrega.
- `captura_testes.png`: captura opcional do terminal, incorporada ao PDF quando presente.

Antes da entrega, inclua uma captura de tela do terminal com a execução dos testes, conforme solicitado pelo enunciado. Para publicar no GitHub, crie um repositório público e envie estes arquivos; o link do repositório deve ser informado na submissão.