import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'KidOS — Personalized Learning',
  description: 'AI-powered educational adventure for kids.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
