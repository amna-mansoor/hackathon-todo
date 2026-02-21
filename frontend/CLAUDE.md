# Frontend Architectural Guidelines (Next.js)

This document outlines the architectural principles and conventions for the Next.js frontend application.

## Core Principles

1.  **Component-Driven Development**: Build UIs from small, isolated, and reusable components.
2.  **App Router First**: Utilize Next.js 16+ App Router for routing and data fetching mechanisms.
3.  **Server Components Preference**: Prefer Server Components for data fetching and rendering where possible to improve performance and reduce client-side bundle size. Use Client Components for interactive UI elements.
4.  **Type Safety**: Strict TypeScript usage across the entire codebase.
5.  **Atomic Design Principles**: Organize components into Atoms, Molecules, Organisms, Templates, and Pages for consistency and scalability.
6.  **Better Auth Integration**: All authentication-related logic must leverage the configured Better Auth library for JWT management and session handling.
7.  **API Call Abstraction**: Centralize API calls through a dedicated client or hook system to ensure consistency, error handling, and type safety.
8.  **Styling with Tailwind CSS**: All styling should be implemented using Tailwind CSS for utility-first styling.
9.  **Accessibility (A11y)**: Ensure all UI components are built with accessibility in mind.
10. **Performance**: Optimize for fast page loads and smooth user interactions.

## Directory Structure

```
frontend/
├── app/                    # Next.js App Router root, containing pages, layouts, and API routes
│   ├── (auth)/             # Grouped routes for authentication (login, register)
│   ├── (dashboard)/        # Grouped routes for authenticated user content (main app)
│   ├── api/                # Next.js API Routes (e.g., for Better Auth callbacks)
│   ├── layout.tsx          # Root layout
│   └── page.tsx            # Root page
├── components/             # Reusable React components (Atoms, Molecules, Organisms)
│   ├── ui/                 # Generic UI components (buttons, inputs)
│   └── tasks/              # Task-specific components
├── lib/                    # Client-side utility functions, API clients, Better Auth config
├── hooks/                  # Custom React hooks
├── public/                 # Static assets
├── styles/                 # Tailwind CSS configuration, global CSS
├── types/                  # TypeScript type definitions for frontend entities
├── tests/                  # Frontend tests (Jest, React Testing Library)
└── package.json            # Project dependencies and scripts
```

## Naming Conventions

-   Components: PascalCase (e.g., `TaskCard.tsx`)
-   Hooks: `use` prefix (e.g., `useTasks.ts`)
-   Functions: camelCase
-   Files: kebab-case for routes, PascalCase for components.

## Data Flow

-   Data fetching on server-side using Server Components or `fetch` API.
-   Mutations handled via Server Actions or client-side API calls.

## Error Handling

-   Display user-friendly error messages in the UI.
-   Log client-side errors appropriately.
