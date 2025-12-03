#!/usr/bin/env python3
"""
Agente para gerar sugestões de imagens para todos os temas.

Este script percorre todas as subpastas em temas/ e para cada tema:
1. Identifica o nome do tema
2. Busca 3-5 imagens relevantes em bancos de imagens gratuitos
3. Cria/atualiza o arquivo sugestoes-imagens.md com a lista de imagens

Bancos de imagens suportados:
- Unsplash (https://unsplash.com)
- Pexels (https://www.pexels.com)
- Pixabay (https://pixabay.com)
"""

import os
import json
import requests
from pathlib import Path
from typing import List, Dict
import time

# Configurações
TEMAS_DIR = Path("temas")
UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"
PEXELS_API_URL = "https://api.pexels.com/v1/search"
PIXABAY_API_URL = "https://pixabay.com/api/"

# Chaves de API (usar variáveis de ambiente para produção)
# Para este projeto educacional, usaremos as APIs públicas sem chave quando possível
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY", "")
PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "")
PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY", "")

# Mapeamento de nomes de temas para palavras-chave em inglês (melhor para busca)
TEMA_KEYWORDS = {
    "catalogo-roupas": ["fashion", "clothing", "clothes", "wardrobe", "style"],
    "empresa": ["technology", "business", "office", "team", "innovation"],
    "ferramenta-online": ["digital", "tools", "technology", "online", "app"],
    "joias": ["jewelry", "jewels", "gold", "diamond", "luxury"],
    "livros": ["books", "library", "reading", "literature", "bookshelf"],
    "midias": ["entertainment", "movies", "games", "media", "streaming"],
    "petshop": ["pet", "dog", "cat", "animals", "veterinary"],
    "projeto-social": ["community", "volunteering", "charity", "social", "help"],
    "receitas": ["food", "cooking", "recipe", "culinary", "kitchen"],
    "viagens": ["travel", "tourism", "destination", "vacation", "adventure"],
}


def get_theme_keyword(theme_name: str) -> str:
    """Retorna a palavra-chave principal para o tema."""
    keywords = TEMA_KEYWORDS.get(theme_name, [theme_name])
    return keywords[0] if keywords else theme_name


def search_unsplash_images(query: str, per_page: int = 5) -> List[Dict]:
    """Busca imagens no Unsplash."""
    images = []
    search_url = f"https://unsplash.com/s/photos/{query}"
    
    # Criar entradas para Unsplash
    image_data = {
        "source": "Unsplash",
        "source_url": "https://unsplash.com",
        "search_url": search_url,
    }
    images.append(image_data)
    
    return images


def search_pexels_images(query: str, per_page: int = 5) -> List[Dict]:
    """Busca imagens no Pexels."""
    images = []
    search_url = f"https://www.pexels.com/search/{query}/"
    
    image_data = {
        "source": "Pexels",
        "source_url": "https://www.pexels.com",
        "search_url": search_url,
    }
    images.append(image_data)
    
    return images


def search_pixabay_images(query: str, per_page: int = 5) -> List[Dict]:
    """Busca imagens no Pixabay."""
    images = []
    search_url = f"https://pixabay.com/images/search/{query}/"
    
    image_data = {
        "source": "Pixabay",
        "source_url": "https://pixabay.com",
        "search_url": search_url,
    }
    images.append(image_data)
    
    return images


def search_freepik_images(query: str) -> List[Dict]:
    """Busca imagens no Freepik."""
    images = []
    search_url = f"https://www.freepik.com/search?format=search&query={query}"
    
    image_data = {
        "source": "Freepik",
        "source_url": "https://www.freepik.com",
        "search_url": search_url,
    }
    images.append(image_data)
    
    return images


def search_burst_images(query: str) -> List[Dict]:
    """Busca imagens no Burst by Shopify."""
    images = []
    # Burst não tem busca direta por URL, então usamos a página principal
    search_url = f"https://burst.shopify.com/photos/search?q={query}"
    
    image_data = {
        "source": "Burst by Shopify",
        "source_url": "https://burst.shopify.com",
        "search_url": search_url,
    }
    images.append(image_data)
    
    return images


def search_images(query: str, num_images: int = 5) -> List[Dict]:
    """
    Busca imagens em múltiplos bancos gratuitos.
    Retorna uma lista mista de diferentes fontes.
    """
    all_images = []
    
    # Buscar no Unsplash
    try:
        unsplash_images = search_unsplash_images(query)
        all_images.extend(unsplash_images)
    except Exception as e:
        print(f"  Erro ao buscar no Unsplash: {e}")
    
    # Buscar no Pexels
    try:
        pexels_images = search_pexels_images(query)
        all_images.extend(pexels_images)
    except Exception as e:
        print(f"  Erro ao buscar no Pexels: {e}")
    
    # Buscar no Pixabay
    try:
        pixabay_images = search_pixabay_images(query)
        all_images.extend(pixabay_images)
    except Exception as e:
        print(f"  Erro ao buscar no Pixabay: {e}")
    
    # Buscar no Freepik
    try:
        freepik_images = search_freepik_images(query)
        all_images.extend(freepik_images)
    except Exception as e:
        print(f"  Erro ao buscar no Freepik: {e}")
    
    # Buscar no Burst
    try:
        burst_images = search_burst_images(query)
        all_images.extend(burst_images)
    except Exception as e:
        print(f"  Erro ao buscar no Burst: {e}")
    
    return all_images


def create_markdown_content(theme_name: str, images: List[Dict]) -> str:
    """
    Cria o conteúdo do arquivo Markdown com as sugestões de imagens.
    """
    # Mapear nomes de temas para português
    theme_names_pt = {
        "catalogo-roupas": "Catálogo de Roupas",
        "empresa": "Empresa de Tecnologia",
        "ferramenta-online": "Ferramenta Online",
        "joias": "Joalheria",
        "livros": "Biblioteca/Livros",
        "midias": "Mídias (Filmes/Séries/Games)",
        "petshop": "Petshop",
        "projeto-social": "Projeto Social",
        "receitas": "Receitas Culinárias",
        "viagens": "Viagens e Turismo",
    }
    
    theme_pt = theme_names_pt.get(theme_name, theme_name.replace("-", " ").title())
    keyword = get_theme_keyword(theme_name)
    
    content = f"""# 📸 Sugestões de Imagens

## Imagens Sugeridas para o tema "{theme_pt}"

Abaixo estão algumas sugestões de imagens de alta qualidade de bancos de imagens gratuitos.
Você pode baixar estas imagens ou buscar outras similares usando as palavras-chave relacionadas ao tema.

**Palavra-chave principal:** `{keyword}`

---

"""
    
    # Adicionar cada banco de imagens
    for i, image in enumerate(images, 1):
        source = image["source"]
        source_url = image["source_url"]
        search_url = image.get("search_url", source_url)
        
        content += f"""### {i}. {source}

[![{source}](https://img.shields.io/badge/{source}-Buscar%20Imagens-blue)]({search_url})

**🔍 Link de Busca:** [{source} - Buscar "{keyword}"]({search_url})

Clique no link acima para buscar imagens gratuitas relacionadas ao tema "{theme_pt}".

**Sobre o {source}:**
- 📸 Milhares de imagens gratuitas de alta qualidade
- ✅ Uso gratuito para projetos pessoais e comerciais
- 📝 Atribuição ao fotógrafo é apreciada (mas nem sempre obrigatória)
- 🌟 Imagens em alta resolução disponíveis

**Fonte:** [{source}]({source_url})

---

"""
    
    # Adicionar instruções finais
    content += """## 📝 Como Usar

1. **Acesse os links acima** e pesquise pelas palavras-chave sugeridas
2. **Baixe as imagens** que mais combinam com seu projeto
3. **Salve as imagens** na pasta `assets/images/` com nomes descritivos
4. **Atualize o arquivo `data.json`** com os nomes corretos das imagens
5. **Verifique a licença** de cada imagem (geralmente é permitido uso gratuito com atribuição)

## 🎨 Dicas de Seleção

- Mantenha **consistência visual** entre todas as imagens
- Prefira **fotos reais** de alta qualidade
- Use imagens com **boa iluminação** e **nitidez**
- Evite imagens com **marcas d'água** muito visíveis
- Considere o **esquema de cores** do seu projeto

## 🔗 Outros Bancos de Imagens Gratuitos

Se não encontrar o que procura nos links acima, experimente:

- **Freepik:** https://www.freepik.com
- **Burst (Shopify):** https://burst.shopify.com
- **Reshot:** https://www.reshot.com
- **StockSnap:** https://stocksnap.io
- **Picjumbo:** https://picjumbo.com

## ⚠️ Importante

Sempre verifique os **termos de uso** de cada imagem. A maioria dos bancos gratuitos permite uso comercial, mas alguns requerem:
- Atribuição ao fotógrafo
- Proibição de revenda
- Limitações de uso

---

**Última atualização:** """ + time.strftime("%d/%m/%Y") + """
"""
    
    return content


def process_theme(theme_path: Path) -> bool:
    """
    Processa um tema: busca imagens e cria o arquivo de sugestões.
    Retorna True se bem-sucedido, False caso contrário.
    """
    theme_name = theme_path.name
    print(f"\n📁 Processando tema: {theme_name}")
    
    # Verificar se existe a pasta assets/images
    images_dir = theme_path / "assets" / "images"
    if not images_dir.exists():
        print(f"  ⚠️  Pasta {images_dir} não existe, criando...")
        images_dir.mkdir(parents=True, exist_ok=True)
    
    # Buscar palavra-chave para o tema
    keyword = get_theme_keyword(theme_name)
    print(f"  🔍 Buscando imagens para: {keyword}")
    
    # Buscar imagens (3-5 imagens)
    num_images = 5
    images = search_images(keyword, num_images)
    
    if not images:
        print(f"  ❌ Nenhuma imagem encontrada para {theme_name}")
        return False
    
    print(f"  ✅ Encontradas {len(images)} sugestões de imagens")
    
    # Criar conteúdo do markdown
    markdown_content = create_markdown_content(theme_name, images)
    
    # Salvar arquivo
    output_file = images_dir / "sugestoes-imagens.md"
    try:
        output_file.write_text(markdown_content, encoding="utf-8")
        print(f"  💾 Arquivo criado: {output_file}")
        return True
    except Exception as e:
        print(f"  ❌ Erro ao criar arquivo: {e}")
        return False


def main():
    """Função principal que processa todos os temas."""
    print("🚀 Iniciando geração de sugestões de imagens...")
    print("=" * 60)
    
    # Verificar se a pasta temas existe
    if not TEMAS_DIR.exists():
        print(f"❌ Erro: Pasta '{TEMAS_DIR}' não encontrada!")
        print(f"   Execute este script da raiz do repositório.")
        return
    
    # Listar todos os temas
    themes = [d for d in TEMAS_DIR.iterdir() if d.is_dir()]
    
    if not themes:
        print(f"❌ Nenhum tema encontrado em '{TEMAS_DIR}'")
        return
    
    print(f"📂 Encontrados {len(themes)} temas:\n")
    
    # Processar cada tema
    success_count = 0
    for theme_path in sorted(themes):
        if process_theme(theme_path):
            success_count += 1
        time.sleep(0.5)  # Pequena pausa entre temas
    
    # Resumo final
    print("\n" + "=" * 60)
    print(f"✅ Processamento concluído!")
    print(f"   {success_count}/{len(themes)} temas processados com sucesso")
    
    if success_count < len(themes):
        print(f"   ⚠️  {len(themes) - success_count} tema(s) com erro")


if __name__ == "__main__":
    main()
