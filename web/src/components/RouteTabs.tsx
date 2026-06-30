import { NavLink } from "react-router-dom";

const TABS = [
  { to: "/consulta", label: "Consulta" },
  { to: "/editor", label: "Editor" },
];

// Badge discreto de navegação entre as páginas — container com borda arredondada,
// usado ao lado do botão "Filtros" (Consulta) e no topo do Editor.
export function RouteTabs() {
  return (
    <div className="inline-flex items-center gap-0.5 rounded-full border border-border bg-muted/50 p-1">
      {TABS.map(({ to, label }) => (
        <NavLink
          key={to}
          to={to}
          className={({ isActive }) =>
            [
              "rounded-full px-3 py-1 text-sm font-medium transition-colors",
              isActive ? "bg-foreground text-background" : "text-muted-foreground hover:bg-card",
            ].join(" ")
          }
        >
          {label}
        </NavLink>
      ))}
    </div>
  );
}
