import { useState, useEffect } from 'react'
import axios from 'axios'
import { motion, AnimatePresence } from 'framer-motion'
import { Code, Box, PieChart, Info, Send, Terminal, Zap, ShieldCheck } from 'lucide-react'

function App() {
    const [code, setCode] = useState(
        `def calculate_sum(n):
    total = 0
    for i in range(n):
        total += i
    return total
`)
    const [result, setResult] = useState(null)
    const [loading, setLoading] = useState(false)
    const [error, setError] = useState(null)

    const handleAnalyze = async () => {
        setLoading(true)
        setError(null)
        try {
            const response = await axios.post('http://localhost:8000/analyze', { code })
            setResult(response.data)
        } catch (err) {
            console.error(err)
            setError("Failed to connect to AI engine. Make sure backend is running.")
        } finally {
            setLoading(false)
        }
    }

    return (
        <div className="container">
            <motion.header
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.8 }}
            >
                <h1>AI-EDN<span>.</span>CORE</h1>
                <p className="subtitle">Premium Intelligent Code Analysis Dashboard</p>
            </motion.header>

            <main className="editor-section">
                {/* Editor Part */}
                <motion.div
                    className="glass-card animate delay-1"
                    initial={{ opacity: 0, scale: 0.95 }}
                    animate={{ opacity: 1, scale: 1 }}
                >
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem', color: 'var(--primary)' }}>
                        <Terminal size={20} />
                        <span style={{ fontWeight: 600, letterSpacing: '1px' }}>SOURCE CODE</span>
                    </div>
                    <textarea
                        value={code}
                        onChange={(e) => setCode(e.target.value)}
                        spellCheck="false"
                    />
                    <button className="btn-primary" onClick={handleAnalyze} disabled={loading}>
                        {loading ? (
                            <div className="loader"></div>
                        ) : (
                            <>
                                <Zap size={18} />
                                Analyze Engine
                            </>
                        )}
                    </button>

                    {error && (
                        <div style={{ marginTop: '1rem', color: '#ff4b2b', fontSize: '0.9rem', textAlign: 'center' }}>
                            {error}
                        </div>
                    )}
                </motion.div>

                {/* Results Panel */}
                <motion.div
                    className="results-panel animate delay-2"
                    initial={{ opacity: 0, x: 20 }}
                    animate={{ opacity: 1, x: 0 }}
                >
                    <AnimatePresence mode="wait">
                        {!result ? (
                            <motion.div
                                key="empty"
                                className="glass-card"
                                style={{ height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', color: 'var(--text-secondary)' }}
                                initial={{ opacity: 0 }}
                                animate={{ opacity: 1 }}
                                exit={{ opacity: 0 }}
                            >
                                <Code size={48} style={{ opacity: 0.2, marginBottom: '1rem' }} />
                                <p>Enter code and trigger analysis</p>
                                <p style={{ fontSize: '0.8rem' }}>AI waiting for input...</p>
                            </motion.div>
                        ) : (
                            <motion.div
                                key="result"
                                className="glass-card"
                                initial={{ opacity: 0, scale: 0.9 }}
                                animate={{ opacity: 1, scale: 1 }}
                                style={{ height: '100%' }}
                            >
                                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1.5rem' }}>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--secondary)' }}>
                                        <PieChart size={20} />
                                        <span style={{ fontWeight: 600, letterSpacing: '1px' }}>AI TUTOR INSIGHTS</span>
                                    </div>
                                    {result.prediction && !result.error && (
                                        <span className={`level-badge level-${result.prediction.level}`}>
                                            {result.prediction.level}
                                        </span>
                                    )}
                                </div>

                                {result.error ? (
                                    <div className="metric-card error-card">
                                        <div className="metric-title" style={{ color: '#ff0055' }}>Syntax Error Detected</div>
                                        <p style={{ fontSize: '0.9rem', marginTop: '0.5rem' }}>{result.message}</p>
                                    </div>
                                ) : (
                                    <>
                                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1rem' }}>
                                            <div className="metric-card">
                                                <div className="metric-title">Loops</div>
                                                <div className="metric-value">{result.features.num_loops}</div>
                                            </div>
                                            <div className="metric-card">
                                                <div className="metric-title">Functions</div>
                                                <div className="metric-value">{result.features.num_functions}</div>
                                            </div>
                                        </div>

                                        <div style={{ marginTop: '1.5rem' }}>
                                            <div className="metric-title">Logic Explanation</div>
                                            <p style={{ fontSize: '0.95rem', color: 'var(--text-secondary)', marginTop: '0.5rem' }}>
                                                {result.prediction.explanation}
                                            </p>
                                        </div>

                                        <div style={{ marginTop: '2rem', padding: '1.5rem', background: 'rgba(255, 255, 255, 0.03)', borderRadius: '12px', border: '1px solid var(--card-border)' }}>
                                            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: 'var(--primary)', marginBottom: '1rem' }}>
                                                <ShieldCheck size={18} />
                                                <span style={{ fontSize: '0.8rem', fontWeight: 800, letterSpacing: '1px' }}>TUTOR RECOMMENDATIONS</span>
                                            </div>
                                            <div style={{ display: 'flex', flexDirection: 'column' }}>
                                                {result.prediction.suggestions.map((tip, i) => (
                                                    <div key={i} className="suggestion-item">{tip}</div>
                                                ))}
                                            </div>
                                        </div>
                                    </>
                                )}
                            </motion.div>
                        )}
                    </AnimatePresence>
                </motion.div>
            </main>

            <footer style={{ marginTop: '4rem', textAlign: 'center', color: 'var(--text-secondary)', fontSize: '0.8rem' }}>
                <p>&copy; 2026 AI-EDN CORE MODULE | HACKATHON EDITION</p>
            </footer>
        </div>
    )
}

export default App
