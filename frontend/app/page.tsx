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
    <div className="min-h-screen bg-purple-50 p-8 font-sans">
      <div className="max-w-4xl mx-auto">
        <header className="flex justify-between items-center mb-12">
            <h1 className="text-4xl font-bold text-purple-800">🚀 KidOS</h1>
            <div className="flex gap-4">
                <div className="w-10 h-10 rounded-full bg-purple-200"></div>
            </div>
        </header>
        
        <main>
            <div className="bg-white p-8 rounded-[40px] shadow-xl border-4 border-purple-100 mb-12 text-center">
                <h2 className="text-2xl font-bold text-gray-800 mb-4">Ready for a new adventure?</h2>
                <button 
                    onClick={startLearning}
                    disabled={loading}
                    className="bg-purple-600 text-white px-10 py-4 rounded-2xl shadow-lg hover:bg-purple-700 transition font-bold text-lg disabled:opacity-50"
                >
                    {loading ? "Discovering..." : "Start Exploring Space!"}
                </button>
            </div>

            <div className="grid gap-6">
                {content.map((card, i) => (
                <div key={i} className="bg-white p-8 rounded-3xl shadow-lg border-2 border-purple-100 hover:scale-[1.02] transition-transform cursor-pointer">
                    <h2 className="text-2xl font-bold text-purple-700 mb-3">{card.title}</h2>
                    <p className="text-gray-600 text-lg leading-relaxed">{card.body}</p>
                </div>
                ))}
            </div>
        </main>
      </div>
    </div>
  );
}
