import React from 'react';
import ChatWidget from '@site/src/components/ChatWidget';
import TranslateButton from '@site/src/components/TranslateButton';

export default function Root({ children }) {
    return (
        <>
            {children}
            <ChatWidget />
            <TranslateButton />
        </>
    );
}
