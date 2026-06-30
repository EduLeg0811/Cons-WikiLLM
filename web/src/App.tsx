import { NavLink, Navigate, Route, Routes } from "react-router-dom";
import { Toaster } from "sonner";
import { ThemeProvider, useTheme } from "./lib/theme";
import { ThemeToggle } from "./components/ThemeToggle";
import { Consulta } from "./routes/Consulta";
import { Editor } from "./routes/Editor";
import favicon from "../favicon.svg";

function NavTab({ to, children }: { to: string; children: string }) {
  return (
    <NavLink
      to={to}
      className={({ isActive }) =>
        [
          "rounded-lg px-3 py-1.5 text-sm font-medium transition-colors",
          isActive ? "bg-primary text-primary-foreground" : "text-muted-foreground hover:bg-muted",
        ].join(" ")
      }
    >
      {children}
    </NavLink>
  );
}

function Shell() {
  const { mode } = useTheme();
  return (
    <div className="min-h-screen">
      <header className="sticky top-0 z-30 border-b border-border/50 bg-background/70 backdrop-blur-xl">
        <div className="mx-auto flex max-w-[1600px] items-center gap-4 px-5 py-4">
          <a
            href="https://www.cons-ia.org"
            target="_blank"
            rel="noopener noreferrer"
            className="group flex items-center gap-2"
          >
            <img
              src={favicon}
              alt=""
              className="h-12 w-12 transition-transform duration-300 group-hover:scale-110
                         group-hover:drop-shadow-[0_0_8px_var(--color-primary)]"
            />
            <span className="text-brand-title">
              Cons <span className="italic text-primary">WikiLLM</span>
            </span>
          </a>
          <nav className="ml-2 flex items-center gap-1">
            <NavTab to="/consulta">Consulta</NavTab>
            <NavTab to="/editor">Editor</NavTab>
          </nav>
          <div className="ml-auto">
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
