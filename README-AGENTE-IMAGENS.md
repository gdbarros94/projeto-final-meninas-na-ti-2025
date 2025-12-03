# 🤖 Agente de Sugestões de Imagens

## 📖 Descrição

Este agente automatiza a criação de arquivos de sugestões de imagens para todos os temas do projeto.

O script `gerar_sugestoes_imagens.py` percorre todas as subpastas em `temas/` e para cada tema:

1. **Identifica o nome do tema** com base na subpasta
2. **Busca 3 a 5 imagens relevantes** em bancos de imagens gratuitos
3. **Cria/atualiza um arquivo Markdown** chamado `sugestoes-imagens.md` dentro de `temas/<nome_do_tema>/assets/images/`

## 🎯 Bancos de Imagens Suportados

O agente gera links de busca para os seguintes bancos de imagens gratuitos:

- **Unsplash** (https://unsplash.com) - Fotos de alta qualidade
- **Pexels** (https://www.pexels.com) - Imagens e vídeos gratuitos
- **Pixabay** (https://pixabay.com) - Fotos e ilustrações
- **Freepik** (https://www.freepik.com) - Recursos gráficos
- **Burst by Shopify** (https://burst.shopify.com) - Imagens para e-commerce

## 🚀 Como Usar

### Pré-requisitos

- Python 3.6 ou superior instalado
- Repositório clonado localmente

### Executar o Agente

1. Navegue até a raiz do repositório:

```bash
cd /caminho/para/projeto-final-meninas-na-ti-2025
```

2. Execute o script:

```bash
python3 gerar_sugestoes_imagens.py
```

ou

```bash
python gerar_sugestoes_imagens.py
```

3. O script irá:
   - Percorrer todas as pastas em `temas/`
   - Criar/atualizar o arquivo `sugestoes-imagens.md` em cada tema
   - Exibir o progresso no terminal

### Saída Esperada

```
🚀 Iniciando geração de sugestões de imagens...
============================================================
📂 Encontrados 10 temas:

📁 Processando tema: catalogo-roupas
  🔍 Buscando imagens para: fashion
  ✅ Encontradas 5 sugestões de imagens
  💾 Arquivo criado: temas/catalogo-roupas/assets/images/sugestoes-imagens.md

📁 Processando tema: petshop
  🔍 Buscando imagens para: pet
  ✅ Encontradas 5 sugestões de imagens
  💾 Arquivo criado: temas/petshop/assets/images/sugestoes-imagens.md

...

============================================================
✅ Processamento concluído!
   10/10 temas processados com sucesso
```

## 📄 Formato do Arquivo Gerado

Cada arquivo `sugestoes-imagens.md` contém:

```markdown
# 📸 Sugestões de Imagens

## Imagens Sugeridas para o tema "Nome do Tema"

**Palavra-chave principal:** `keyword`

---

### 1. Unsplash

[![Unsplash](badge)](link)

**🔍 Link de Busca:** [Unsplash - Buscar "keyword"](link)

**Sobre o Unsplash:**
- 📸 Milhares de imagens gratuitas de alta qualidade
- ✅ Uso gratuito para projetos pessoais e comerciais
- 📝 Atribuição ao fotógrafo é apreciada (mas nem sempre obrigatória)
- 🌟 Imagens em alta resolução disponíveis

**Fonte:** [Unsplash](https://unsplash.com)

---

[... mais 4 fontes de imagens ...]

## 📝 Como Usar
## 🎨 Dicas de Seleção
## 🔗 Outros Bancos de Imagens Gratuitos
## ⚠️ Importante
```

## 🎨 Palavras-Chave por Tema

O agente usa as seguintes palavras-chave em inglês para buscar imagens relevantes:

| Tema | Palavra-chave Principal |
|------|------------------------|
| catalogo-roupas | fashion |
| empresa | technology |
| ferramenta-online | digital |
| joias | jewelry |
| livros | books |
| midias | entertainment |
| petshop | pet |
| projeto-social | community |
| receitas | food |
| viagens | travel |

## 🔧 Personalização

Para adicionar novos temas ou modificar palavras-chave:

1. Abra o arquivo `gerar_sugestoes_imagens.py`
2. Localize o dicionário `TEMA_KEYWORDS`
3. Adicione ou modifique as entradas:

```python
TEMA_KEYWORDS = {
    "nome-do-tema": ["palavra1", "palavra2", "palavra3"],
    # ... outros temas
}
```

## 📁 Estrutura de Arquivos

```
projeto-final-meninas-na-ti-2025/
├── gerar_sugestoes_imagens.py       # Script do agente
├── README-AGENTE-IMAGENS.md         # Este arquivo
└── temas/
    ├── catalogo-roupas/
    │   └── assets/
    │       └── images/
    │           └── sugestoes-imagens.md  # Gerado pelo agente
    ├── petshop/
    │   └── assets/
    │       └── images/
    │           └── sugestoes-imagens.md  # Gerado pelo agente
    └── ...
```

## ✅ Benefícios

- **Automação:** Gera arquivos para todos os temas de uma vez
- **Consistência:** Formato padronizado em todos os temas
- **Facilidade:** Links diretos para busca em bancos de imagens
- **Educacional:** Ensina alunas onde encontrar imagens gratuitas
- **Atualização fácil:** Re-execute o script para atualizar todos os arquivos

## 🆘 Solução de Problemas

### Erro: "Pasta 'temas' não encontrada"

**Solução:** Execute o script da raiz do repositório, não de dentro de uma subpasta.

### Erro: "Python não reconhecido"

**Solução:** Instale o Python 3 ou verifique se está no PATH do sistema.

### Arquivo não está sendo criado

**Solução:** 
- Verifique se a pasta `assets/images/` existe no tema
- O script cria a pasta automaticamente se não existir
- Verifique permissões de escrita no diretório

## 📝 Notas Importantes

- O script **sobrescreve** arquivos existentes sem avisar
- É seguro executar múltiplas vezes
- Não requer conexão com internet (apenas gera links de busca)
- Não faz download de imagens (apenas cria referências)
- As alunas ainda precisam baixar as imagens manualmente

## 🤝 Contribuindo

Para melhorar o agente:

1. Adicione mais bancos de imagens na função `search_images()`
2. Melhore as palavras-chave em `TEMA_KEYWORDS`
3. Personalize o template Markdown em `create_markdown_content()`
4. Adicione suporte para múltiplos idiomas

## 📜 Licença

Este script faz parte do projeto educacional Meninas na TI 2025.

---

**Desenvolvido com 💜 para as Meninas na TI 2025**
