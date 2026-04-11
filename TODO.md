# TODO

## Thumbnails pendents (ollama MLX trencat post-update sistema)

El problema: `libmlxc.dylib not found` — el runner MLX d'ollama no funciona des de l'actualització del sistema.
Solució quan funcioni: `sudo ln -sf /Applications/Ollama.app/Contents/Resources/mlx_metal_v4/libmlxc.dylib /usr/local/lib/libmlxc.dylib`

### Episodi 005
```bash
python scripts/generate_thumbnail.py \
  --episodi 005 \
  --nom 005-ouro-ia-pensa-en-bucle \
  --prompt-suffix "a small glowing brain looping inside a recursive loop of light, ouroboros snake eating its tail in the background, futuristic neon"
```
Afegir al frontmatter de `_episodes/005-ouro-ia-pensa-en-bucle.md`:
```yaml
thumbnail: "/assets/thumbnails/005-ouro-ia-pensa-en-bucle.png"
```

### Episodi 006
```bash
python scripts/generate_thumbnail.py \
  --episodi 006 \
  --nom 006-raonament-autonom-claude-mythos \
  --prompt-suffix "a glowing TARDIS with a cracked door leaking light, classified documents floating around, neural network nodes forming a brain in the vortex background"
```
Afegir al frontmatter de `_episodes/006-raonament-autonom-claude-mythos.md`:
```yaml
thumbnail: "/assets/thumbnails/006-raonament-autonom-claude-mythos.png"
```
