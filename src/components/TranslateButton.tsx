import React, { useState } from 'react';
import styles from './TranslateButton.module.css';

export default function TranslateButton() {
    const [translating, setTranslating] = useState(false);
    const [urduText, setUrduText] = useState('');

    const handleTranslate = async () => {
        // Find the main documentation content
        const article = document.querySelector('article');
        if (!article) {
            alert('No documentation content found on this page.');
            return;
        }

        // Get text while excluding code blocks and some UI elements if possible
        // For a hackathon demo, innerText of article is usually sufficient
        const textToTranslate = article.innerText;

        setTranslating(true);
        try {
            const response = await fetch('http://localhost:8000/api/translate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: textToTranslate }),
            });

            if (!response.ok) throw new Error('Backend error');

            const data = await response.json();
            setUrduText(data.translated_text);
        } catch (error) {
            console.error('Translation failed:', error);
            alert('Translation failed. Make sure the backend is running.');
        } finally {
            setTranslating(false);
        }
    };

    if (urduText) {
        return (
            <div className={styles.urduOverlay}>
                <button onClick={() => setUrduText('')} className={styles.closeBtn}>
                    Close Translation / بند کریں
                </button>
                <div className={styles.urduContent}>
                    {urduText}
                </div>
            </div>
        );
    }

    return (
        <button
            onClick={handleTranslate}
            className={styles.translateBtn}
            disabled={translating}
            title="Translate this page to Urdu (AI Bonus Feature)"
        >
            {translating ? (
                <>
                    <span className={styles.spinner}></span> Translating...
                </>
            ) : (
                'Urdu Translation (اردو)'
            )}
        </button>
    );
}
