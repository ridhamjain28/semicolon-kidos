'use client';
import { useState } from 'react';
import { api } from '../services/api';

export default function Home() {
  const [content, setContent] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  const startLearning = async () => {
    setLoading(true);
    try {
        const data = await api.fetchContent("Space", 8);
        setContent(data);
    } catch (err) {
        console.error("Failed to load content", err);
    } finally {
        setLoading(false);
    }
  };

  return (
    <div className="min-h-screen p-6 md:p-12">
      <div className="max-w-5xl mx-auto">
        <header className="flex justify-between items-center mb-16 animate-pop">
            <div className="flex items-center gap-4">
                <div className="w-14 h-14 rounded-3xl bg-gradient-to-tr from-purple-600 to-pink-500 text-white flex items-center justify-center text-3xl shadow-xl transform rotate-3">
                    🌟
                </div>
                <h1 className="text-4xl font-extrabold tracking-tight text-gray-900">
                    Kid<span className="text-purple-600">OS</span>
                </h1>
            </div>
            <div className="flex items-center gap-4 glass-card px-4 py-2 rounded-2xl">
                <span className="font-bold text-purple-700">Explorer Points: 150 ⭐</span>
            </div>
        </header>
        
        <main>
            <div className="glass-card p-10 md:p-16 rounded-[50px] mb-16 text-center border-white/50 relative overflow-hidden group">
                <div className="absolute top-0 left-0 w-full h-2 bg-gradient-to-right from-purple-500 to-pink-500"></div>
                <h2 className="text-3xl md:text-5xl font-black text-gray-900 mb-6 leading-tight">
                    Where shall we <span className="text-gradient">explore</span> today?
                </h2>
                <p className="text-xl text-gray-600 mb-10 max-w-2xl mx-auto font-medium">
                    The universe is full of mysteries waiting for a curious explorer like you!
                </p>
                <button 
                    onClick={startLearning}
                    disabled={loading}
                    className="bg-purple-600 text-white px-12 py-5 rounded-[24px] kid-shadow hover:bg-purple-700 transition-all font-black text-xl disabled:opacity-50 active:scale-95"
                >
                    {loading ? "Discovering..." : "Launch to Space! 🚀"}
                </button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
                {content.map((card, i) => (
                <div 
                    key={i} 
                    style={{ animationDelay: `${i * 0.1}s` }}
                    className="glass-card p-10 rounded-[40px] animate-pop hover:scale-[1.03] transition-all cursor-pointer group relative"
                >
                    <div className="absolute top-6 right-8 text-4xl opacity-20 group-hover:opacity-100 transition-opacity">🛸</div>
                    <h2 className="text-2xl font-black text-purple-800 mb-4 pr-12">{card.title}</h2>
                    <p className="text-gray-700 text-lg leading-relaxed font-medium">{card.body}</p>
                    <div className="mt-8 flex gap-3">
                        <span className="px-4 py-2 bg-purple-100 text-purple-700 rounded-full text-sm font-bold">Science</span>
                        <span className="px-4 py-2 bg-pink-100 text-pink-700 rounded-full text-sm font-bold">Space</span>
                    </div>
                </div>
                ))}
            </div>
        </main>
      </div>
    </div>
  );
}
