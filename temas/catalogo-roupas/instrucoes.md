# 👗 Tema: Catálogo de Roupas / Moda

## 📝 Descrição do Tema

Este tema é ideal para criar um **catálogo online de roupas e acessórios de moda**. Você pode usá-lo para:
- Loja de roupas femininas, masculinas ou infantis
- Boutique online
- Coleção de moda autoral
- Brechó virtual
- Lookbook de tendências

---

## 🎯 Objetivo do Site

Criar uma página onepage atraente que:
1. Apresente sua marca/loja de forma elegante
2. Exiba produtos de moda com imagens de qualidade
3. Permita que visitantes se cadastrem para receber novidades
4. Seja responsivo e funcione bem em dispositivos móveis

---

## 📁 Arquivos que Você Deve Editar

### 1. `index.html`
**O que personalizar:**
- **Linha 6:** Alterar o título da página
  ```html
  <title>Sua Loja - Catálogo de Moda</title>
  ```
- **Linha 24:** Nome da sua loja/marca
  ```html
  <a class="navbar-brand" href="#">Boutique Elegance</a>
  ```
- **Linhas 48-50:** Título e subtítulo do Hero
  ```html
  <h1>Sua Moda, Seu Estilo</h1>
  <p>Descubra a coleção perfeita para você</p>
  ```
- **Linha 57:** Título da seção de produtos
  ```html
  <h2>Nossa Coleção</h2>
  ```
- **Linha 69:** Título do formulário
  ```html
  <h2>Cadastre-se e Receba Novidades</h2>
  ```

### 2. `data.json` (na pasta `dados/`)
**Como usar:**
Este arquivo já contém 8 peças de roupa como exemplo. Você pode:
- **Manter os dados atuais** e apenas trocar as imagens
- **Adicionar mais produtos** seguindo o mesmo formato
- **Personalizar** títulos e descrições para sua coleção

**Estrutura do JSON:**
```json
{
  "titulo": "Nome da Peça",
  "descricao": "Descrição detalhada da roupa",
  "imagem": "assets/images/nome-arquivo.jpg"
}
```

### 3. `style.css`
**Personalização de cores:**
- **Linhas 24-25:** Altere o gradiente do header
  ```css
  background: linear-gradient(135deg, #FFB6C1 0%, #9B59B6 100%);
  ```
- **Linha 38:** Altere o gradiente do hero
  ```css
  background: linear-gradient(135deg, #FFB6C1 0%, #9B59B6 100%);
  ```
- **Linha 162:** Cor dos botões
  ```css
  background: linear-gradient(135deg, #9B59B6 0%, #8E44AD 100%);
  ```

**Fontes:** O tema usa:
- **Playfair Display** para títulos (elegante e sofisticada)
- **Open Sans** para textos (moderna e legível)

Para mudar, visite [Google Fonts](https://fonts.google.com/) e substitua no HTML (linha 13-14).

---

## 🖼️ Como Usar as Imagens

### Imagens Necessárias:

1. **hero.jpg** - Imagem principal do topo (1920x1080px recomendado)
2. **vestido-floral.jpg** - Produto 1
3. **calca-jeans.jpg** - Produto 2
4. **blusa-branca.jpg** - Produto 3
5. **jaqueta-jeans.jpg** - Produto 4
6. **saia-plissada.jpg** - Produto 5
7. **conjunto-moletom.jpg** - Produto 6
8. **blazer-preto.jpg** - Produto 7
9. **vestido-longo.jpg** - Produto 8

### Onde Baixar Imagens Gratuitas:

**Unsplash:** https://unsplash.com/
- Busque por: "fashion", "clothing", "dress", "style"
- Todas as imagens são gratuitas e de alta qualidade

**Pexels:** https://www.pexels.com/
- Busque por: "moda", "roupa", "fashion", "outfit"
- Download gratuito sem necessidade de atribuição

### Como Adicionar:
1. Baixe as imagens
2. Renomeie conforme os nomes acima
3. Coloque na pasta `assets/images/`
4. O JavaScript carregará automaticamente do `data.json`

---

## 📝 Onde Inserir o Formulário

O formulário já está incluído na seção de contato (linhas 64-85 do `index.html`).

**Campos atuais:**
- Nome Completo
- E-mail
- Telefone (opcional)
- Mensagem

**Para personalizar para Newsletter:**
```html
<div class="mb-3">
    <label for="nome" class="form-label">Seu Nome</label>
    <input type="text" class="form-control" id="nome" required>
</div>
<div class="mb-3">
    <label for="email" class="form-label">Seu Melhor E-mail</label>
    <input type="email" class="form-control" id="email" required>
</div>
<div class="mb-3">
    <div class="form-check">
        <input class="form-check-input" type="checkbox" id="aceito" required>
        <label class="form-check-label" for="aceito">
            Aceito receber novidades e promoções
        </label>
    </div>
</div>
<button type="submit" class="btn btn-primary btn-lg w-100">Quero Receber Novidades</button>
```

---

## ✨ Onde Inserir as Animações

### Animação CSS (Hover nos Cards)
Já está implementada no `style.css` (linhas 112-115).

**Como funciona:**
Quando você passa o mouse sobre um card de produto, ele:
- Sobe suavemente (`translateY(-10px)`)
- Ganha uma sombra maior

**Para personalizar:**
```css
.produto-card:hover {
    transform: translateY(-15px); /* Aumenta o efeito */
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.3); /* Sombra mais forte */
}
```

### Animação JavaScript (Scroll Reveal)
Já está implementada no `script.js` (linhas 45-59).

**Como funciona:**
Elementos com a classe `.reveal` aparecem suavemente quando você rola a página até eles.

**Onde usar:**
Adicione a classe `reveal` em qualquer elemento que deve aparecer ao rolar:
```html
<div class="col-md-4 reveal">
    <!-- conteúdo -->
</div>
```

**Já está aplicado em:**
- Cards de produtos (aparecem ao rolar)

---

## 🎨 Como Personalizar Sem Quebrar a Base

### ✅ Pode Fazer:
- Alterar cores no CSS
- Mudar textos no HTML
- Adicionar mais produtos no JSON
- Trocar imagens
- Ajustar tamanhos de fonte
- Adicionar mais campos no formulário
- Mudar as fontes do Google Fonts

### ❌ Evite:
- Remover links do Bootstrap e fontes do `<head>`
- Apagar o arquivo `script.js`
- Mudar a estrutura do JSON (sempre use: titulo, descricao, imagem)
- Remover IDs dos elementos (são usados pelo JavaScript)
- Alterar a função `carregarProdutos()` no JavaScript

### 💡 Dica:
Sempre faça uma cópia do arquivo original antes de editar. Se algo quebrar, você pode voltar!

---

## ✅ CHECKLIST OBRIGATÓRIO DE ENTREGA

Certifique-se de que seu projeto contém:

### Estrutura Básica
- [ ] Página onepage completa (index.html)
- [ ] Mínimo de 2 blocos de conteúdo (produtos + formulário)
- [ ] Header fixo com navegação
- [ ] Footer com informações

### Conteúdo
- [ ] Hero section com título e subtítulo personalizados
- [ ] Mínimo de 5 produtos no catálogo
- [ ] Imagens reais de roupas/moda
- [ ] Textos personalizados (não deixar "Exemplo")

### Formulário
- [ ] Formulário funcional com no mínimo 3 campos
- [ ] Labels descritivos
- [ ] Botão de envio personalizado
- [ ] Validação básica (campos required)

### Tecnologias
- [ ] Bootstrap implementado
- [ ] CSS personalizado com suas cores
- [ ] 1 animação CSS funcionando (hover nos cards)
- [ ] 1 animação JavaScript funcionando (scroll reveal)

### Dados Dinâmicos
- [ ] Arquivo data.json preenchido corretamente
- [ ] Produtos sendo carregados via JavaScript
- [ ] Estrutura JSON correta (titulo, descricao, imagem)

### Estilo
- [ ] Paleta de cores coerente (consulte layout.md)
- [ ] Fontes do Google Fonts aplicadas
- [ ] Layout responsivo (funciona em mobile)

### Qualidade
- [ ] Todas as imagens estão carregando
- [ ] Não há erros no Console (F12)
- [ ] Código HTML válido
- [ ] Ortografia correta nos textos

---

## 🔗 Links Úteis Específicos para Moda

### Imagens Gratuitas
- **Unsplash Fashion:** https://unsplash.com/s/photos/fashion
- **Pexels Clothing:** https://www.pexels.com/search/clothing/
- **Pixabay Style:** https://pixabay.com/images/search/style/

### Inspiração de Cores
- **Coolors (paletas de moda):** https://coolors.co/palettes/trending
- **Adobe Color:** https://color.adobe.com/pt/explore

### Fontes Elegantes para Moda
- **Playfair Display:** Elegante, serifada
- **Cormorant Garamond:** Clássica, sofisticada
- **Montserrat:** Moderna, clean
- **Cinzel:** Luxuosa, premium

### Ícones
- **Font Awesome:** https://fontawesome.com/ (ícones de redes sociais, carrinho)
- **Feather Icons:** https://feathericons.com/ (ícones minimalistas)

---

## 🆘 Problemas Específicos e Soluções

### ❌ As imagens dos produtos aparecem quebradas
**Solução:**
- Verifique se as imagens estão na pasta `assets/images/`
- Confirme que os nomes no `data.json` correspondem aos nomes dos arquivos
- Use o caminho relativo correto: `assets/images/nome.jpg`

### ❌ O layout não está elegante como no exemplo
**Solução:**
- Use imagens de alta qualidade (mínimo 800x600px)
- Mantenha consistência nas proporções das fotos
- Aplique as cores sugeridas no `layout.md`

### ❌ Os cards estão desalinhados no mobile
**Solução:**
- Certifique-se de que o Bootstrap está carregando
- Use as classes corretas: `col-12 col-md-6 col-lg-4`

---

## 💬 Dica Final

Este tema é perfeito para criar um **portfólio de moda**, **loja virtual** ou **lookbook**. 

**Seja criativa!** Você pode:
- Criar coleções temáticas (Verão, Inverno, Festa)
- Adicionar seções extras (Sobre a Marca, Depoimentos)
- Incluir filtros por categoria (Vestidos, Calças, Acessórios)

**Boa sorte com sua loja de moda! 👗✨**
