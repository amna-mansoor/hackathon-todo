// [Task]: T012
// [From]: speckit.plan / Phase 1: Project Setup & Monorepo Configuration
// [Spec]: spec-kit/specs/features/authentication.md

// Placeholder for Better Auth configuration (e.g., NextAuth.js setup)
// This file will contain the configuration for authentication providers, callbacks, and session management.

// import NextAuth from "next-auth";
// import Providers from "next-auth/providers";

// export default NextAuth({
//   providers: [
//     Providers.Credentials({
//       name: "Credentials",
//       credentials: {
//         email: { label: "Email", type: "text" },
//         password: { label: "Password", type: "password" },
//       },
//       async authorize(credentials, req) {
//         // Add logic here to authenticate the user and return user object
//         // e.g., call your backend API
//         const res = await fetch("http://localhost:8000/auth/login", {
//           method: "POST",
//           body: JSON.stringify(credentials),
//           headers: { "Content-Type": "application/json" },
//         });
//         const user = await res.json();

//         if (res.ok && user) {
//           return user;
//         }
//         // If no error was thrown and no user data was returned, we send an error response
//         return null;
//       },
//     }),
//   ],
//   session: {
//     jwt: true,
//   },
//   callbacks: {
//     async jwt(token, user) {
//       if (user) {
//         token.id = user.id;
//       }
//       return token;
//     },
//     async session(session, token) {
//       session.user.id = token.id;
//       return session;
//     },
//   },
//   // ... other NextAuth.js configurations
// });
