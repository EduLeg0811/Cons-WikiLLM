import Markdown, { defaultUrlTransform } from "react-markdown";
import remarkGfm from "remark-gfm";

// Converte os links estilo Obsidian em links markdown com protocolo "wiki:".
//   [[slug|texto]] -> [texto](wiki:slug)
//   [[slug]]       -> [slug](wiki:slug)
function preprocess(body: string): string {
  return body
    .replace(/\[\[([^\]|]+)\|([^\]]+)\]\]/g, (_, s, t) => `[${t}](wiki:${s.trim()})`)
    .replace(/\[\[([^\]]+)\]\]/g, (_, s) => `[${s.trim()}](wiki:${s.trim()})`);
}

export function MarkdownReader({
  body,
  onOpenSlug,
}: {
  body: string;
  onOpenSlug: (slug: string) => void;
}) {
  return (
    <div className="prose-wiki">
      <Markdown
        remarkPlugins={[remarkGfm]}
        // Preserva o protocolo "wiki:" (a sanitização padrão o descartaria);
        // demais URLs seguem o saneamento normal contra javascript:/data: etc.
        urlTransform={(url) => (url.startsWith("wiki:") ? url : defaultUrlTransform(url))}
        components={{
          a({ href, children, node: _node, ...rest }) {
            if (href?.startsWith("wiki:")) {
              const slug = href.slice(5);
              return (
                <button
                  type="button"
                  onClick={() => onOpenSlug(slug)}
                  className="font-medium text-primary underline-offset-2 hover:underline"
                >
                  {children}
                </button>
              );
            }
            return (
              <a href={href} target="_blank" rel="noreferrer" className="text-primary hover:underline" {...rest}>
                {children}
              </a>
            );
          },
        }}
      >
        {preprocess(body)}
      </Markdown>
    </div>
  );
}
