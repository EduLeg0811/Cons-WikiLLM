import { Navigate, Route, Routes } from "react-router-dom";
import { Toaster } from "sonner";
import { ThemeProvider, useTheme } from "./lib/theme";
import { ThemeToggle } from "./components/ThemeToggle";
import { Consulta } from "./routes/Consulta";
import { Editor } from "./routes/Editor";
import favicon from "../favicon.svg";

function Shell() {
  const { mode } = useTheme();
  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-30 border-b border-border/50 bg-card/70 backdrop-blur-xl">
        <div className="mx-auto flex max-w-[1600px] items-center gap-4 px-6 py-5">
          <a
            href="https://cons-ia-gallery.onrender.com/gallery.html"
            target="_blank"
            rel="noopener noreferrer"
            title="Voltar à página inicial"
            className="group flex items-center gap-3"
          >
            <img
              src={favicon}
              alt=""
              className="h-12 w-12 transition-transform duration-300 group-hover:scale-110
                         group-hover:drop-shadow-[0_0_8px_color-mix(in_oklch,var(--color-primary)_40%,transparent)]"
            />
            <span className="flex items-center gap-5">
              <span className="font-display max-w-[14rem] truncate text-3xl font-medium tracking-tight text-foreground sm:max-w-none">
                Cons <span className="italic text-primary">Wiki</span>
              </span>
              <span className="hidden h-6 w-px bg-border sm:inline" />
              <span className="hidden font-sans text-xs uppercase tracking-[0.22em] text-muted-foreground sm:inline">
                Wiki LLM de Conscienciologia
              </span>
            </span>
          </a>
          <div className="ml-auto flex items-center gap-2">
            <ThemeToggle />
          </div>
        </div>
      </header>

      <main className="mx-auto max-w-[1600px] px-5 py-5">
        <Routes>
          <Route path="/" element={<Navigate to="/consulta" replace />} />
          <Route path="/consulta" element={<Consulta />} />
          <Route path="/editor" element={<Editor />} />
          <Route path="*" element={<Navigate to="/consulta" replace />} />
        </Routes>
      </main>

      <Toaster theme={mode} richColors position="bottom-right" />
    </div>
  );
}

export function App() {
  return (
    <ThemeProvider>
      <Shell />
    </ThemeProvider>
  );
}
