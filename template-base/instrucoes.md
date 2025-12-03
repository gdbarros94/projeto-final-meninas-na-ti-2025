# 📚 Instruções de Uso do Template Base

## 🎯 O que é este template?

Este é um template base completo e funcional para você começar seu projeto final. Ele já inclui:
- ✅ HTML estruturado com Bootstrap
- ✅ CSS com animações
- ✅ JavaScript com consumo de dados JSON
- ✅ Estrutura responsiva
- ✅ Formulário funcional

---

## 🚀 Como usar este template

### 1️⃣ **Copie os arquivos para sua pasta de tema**

Você deve escolher um tema na pasta `/temas/` e copiar estes arquivos para lá:

```bash
cp template-base/* temas/SEU-TEMA/
```

### 2️⃣ **Personalize o conteúdo do HTML (index.html)**

Edite o arquivo `index.html` e personalize:

- **Título da página** (linha 6): Mude "Template Base" para o nome do seu projeto
- **Nome do site** (linha 24): Mude "Meu Projeto" para o nome do seu tema
- **Hero Section** (linhas 46-51): 
  - Título: Altere "Bem-vindo ao Meu Projeto"
  - Subtítulo: Altere para descrever seu projeto
- **Seção de Produtos** (linha 57): Mude "Nossos Produtos" para algo relacionado ao seu tema
- **Footer** (linhas 88-119): Adicione informações relevantes ao seu projeto

### 3️⃣ **Edite os dados do JSON (data.json)**

Abra o arquivo `data.json` e substitua os produtos de exemplo pelos seus próprios dados:

```json
[
  {
    "titulo": "Nome do Item",
    "descricao": "Descrição completa do item",
    "imagem": "caminho/para/imagem.jpg"
  }
]
```

**Importante:**
- Mantenha a mesma estrutura (titulo, descricao, imagem)
- Adicione de 5 a 8 itens
- As imagens devem estar na pasta `assets/images/`

### 4️⃣ **Personalize as cores e estilos (style.css)**

No arquivo `style.css`, você pode personalizar:

**Cores principais** (linhas 22-23):
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```
Substitua `#667eea` e `#764ba2` pelas cores do seu tema.

**Fontes** (linha 10):
```css
font-family: 'Poppins', sans-serif;
```
Visite [Google Fonts](https://fonts.google.com/) e escolha outras fontes se preferir.

### 5️⃣ **Adicione suas imagens**

1. Coloque todas as imagens na pasta `assets/images/`
2. Use nomes descritivos: `hero.jpg`, `card-01.jpg`, `card-02.jpg`, etc.
3. Atualize os caminhos no `data.json`

---

## 🎨 Entendendo as Animações

### ✨ **Animação CSS: Fade In**

Localizada no `style.css` (linhas 88-101), ela faz elementos aparecerem suavemente:

```css
.fade-in {
    animation: fadeIn 1s ease-in;
}
```

**Onde usar:** Adicione a classe `fade-in` em qualquer elemento HTML.

### ✨ **Animação CSS: Hover nos Cards**

Localizada no `style.css` (linhas 112-115), faz os cards subirem ao passar o mouse:

```css
.produto-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}
```

**Como personalizar:** Altere o valor `-10px` para subir mais ou menos.

### ✨ **Animação JavaScript: Scroll Reveal**

Localizada no `script.js` (linhas 58-74), faz elementos aparecerem ao rolar a página:

```javascript
function ativarAnimacoesScroll() {
    const elementos = document.querySelectorAll('.reveal');
    // ...
}
```

**Onde usar:** Adicione a classe `reveal` em elementos que devem aparecer no scroll.

---

## 📋 Como Consumir o JSON

O arquivo `script.js` já está configurado para consumir o `data.json`:

```javascript
async function carregarProdutos() {
    const response = await fetch('data.json');
    const produtos = await response.json();
    renderizarProdutos(produtos);
}
```

**O que acontece:**
1. O JavaScript busca os dados do `data.json`
2. Converte em objetos JavaScript
3. Cria cards automaticamente para cada produto
4. Exibe na seção de produtos

**Para adicionar mais dados:**
- Edite apenas o `data.json`
- O JavaScript cuidará do resto automaticamente

---

## 🎯 Como Usar o Bootstrap

O Bootstrap já está incluído! Você pode usar seus componentes:

### Exemplos de componentes úteis:

**Botões:**
```html
<button class="btn btn-primary">Clique aqui</button>
<button class="btn btn-success">Sucesso</button>
<button class="btn btn-danger">Perigo</button>
```

**Grid System:**
```html
<div class="row">
    <div class="col-md-6">Coluna 1</div>
    <div class="col-md-6">Coluna 2</div>
</div>
```

**Cards:**
```html
<div class="card">
    <div class="card-body">
        <h5 class="card-title">Título</h5>
        <p class="card-text">Texto</p>
    </div>
</div>
```

📖 **Documentação completa:** [getbootstrap.com](https://getbootstrap.com/)

---

## ✅ CHECKLIST DE ENTREGA OBRIGATÓRIA

Seu projeto DEVE conter:

- [ ] **Página onepage completa** (todas as seções em um único arquivo HTML)
- [ ] **Mínimo de 2 blocos de conteúdo** (já tem: produtos + formulário)
- [ ] **Um bloco com formulário** (já incluído na seção de contato)
- [ ] **1 animação CSS** (já incluída: fade-in e hover)
- [ ] **1 animação JavaScript** (já incluída: scroll reveal)
- [ ] **Conteúdo consumido via JSON** (já configurado em `data.json`)
- [ ] **Uso do Bootstrap** (já incluído via CDN)
- [ ] **Responsividade** (já implementada)
- [ ] **Imagens reais do seu tema** (você precisa adicionar)
- [ ] **Conteúdo personalizado** (você precisa editar os textos)

---

## 🎨 Onde Colocar Cada Elemento

### Header (Topo fixo)
- **Localização:** Linhas 18-39 do `index.html`
- **O que editar:** Nome da marca e itens do menu

### Hero (Seção principal)
- **Localização:** Linhas 42-51 do `index.html`
- **O que editar:** Título, subtítulo e texto do botão
- **Dica:** Você pode adicionar uma imagem de fundo no CSS

### Bloco de Cards/Produtos
- **Localização:** Linhas 54-61 do `index.html`
- **O que editar:** Título da seção
- **Dados:** Vêm do `data.json` automaticamente

### Formulário
- **Localização:** Linhas 64-85 do `index.html`
- **O que editar:** Labels e campos conforme necessidade
- **Dica:** Mantenha ao menos 3 campos

### Footer (Rodapé)
- **Localização:** Linhas 88-119 do `index.html`
- **O que editar:** Links e informações da empresa/projeto

---

## 🆘 Problemas Comuns e Soluções

### ❌ Os produtos não aparecem
**Solução:** 
- Verifique se o arquivo `data.json` está na mesma pasta que o `index.html`
- Abra o Console do navegador (F12) para ver erros

### ❌ As animações não funcionam
**Solução:**
- Verifique se o `script.js` está carregando (veja no final do HTML)
- Certifique-se de que as classes `fade-in` e `reveal` estão nos elementos corretos

### ❌ O CSS não está aplicando
**Solução:**
- Confirme que o arquivo `style.css` está na mesma pasta
- Limpe o cache do navegador (Ctrl + F5)

### ❌ O formulário não envia
**Solução:**
- O formulário atual apenas mostra um alerta
- Para enviar dados reais, você precisaria de um backend (fora do escopo)

---

## 🔗 Links Úteis

- **Bootstrap:** https://getbootstrap.com/
- **Google Fonts:** https://fonts.google.com/
- **Placeholder de Imagens:** https://placeholder.com/
- **Unsplash (imagens gratuitas):** https://unsplash.com/
- **MDN Web Docs:** https://developer.mozilla.org/

---

## 💡 Dicas Finais

1. **Teste sempre no navegador** após fazer alterações
2. **Use o Console (F12)** para ver erros de JavaScript
3. **Valide seu HTML** em https://validator.w3.org/
4. **Faça commits frequentes** se estiver usando Git
5. **Peça ajuda** se algo não funcionar!

**Boa sorte com seu projeto! 🚀**
