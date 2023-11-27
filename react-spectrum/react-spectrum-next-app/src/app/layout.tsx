import type { Metadata } from "next";
import { App } from "./app";
import "./globals.css";

export const metadata: Metadata = {
  title: "UI Library Comparison",
  description: "Comparing various UI component libraries by building forms",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <App>{children}</App>
      </body>
    </html>
  );
}
