/**
 * API Configuration
 * Determines the backend API URL based on environment
 * 
 * IMPORTANT: For production deployment, update PRODUCTION_API_URL below
 * with your actual backend URL (e.g., from Railway, Render, etc.)
 */

// ============================================
// CONFIGURATION: Set your production backend URL here
// ============================================
// Examples:
// - Railway: 'https://your-app-name.railway.app'
// - Render: 'https://your-app-name.onrender.com'
// - Custom: 'https://api.yourdomain.com'
// Leave empty to use same origin (if backend is on same domain)
const PRODUCTION_API_URL = 'https://hackathon-book-documnetation.vercel.app/'; // <-- UPDATE THIS with your backend URL

/**
 * Get the API base URL based on current environment
 */
const getApiUrl = (): string => {
  // Check if we're in browser environment
  if (typeof window === 'undefined') {
    // Server-side rendering: use default
    return 'http://localhost:8000';
  }

  // Check if we're on localhost (development)
  const isLocalhost = window.location.hostname === 'localhost' || 
                      window.location.hostname === '127.0.0.1' ||
                      window.location.hostname === '';

  if (isLocalhost) {
    return 'http://localhost:8000';
  }

  // Production: use configured URL
  if (PRODUCTION_API_URL) {
    return PRODUCTION_API_URL;
  }

  // Fallback: try same origin (if backend is on same domain)
  // If your backend is on a different domain, you MUST set PRODUCTION_API_URL above
  console.warn(
    'API_BASE_URL: PRODUCTION_API_URL not set. Using same origin as fallback. ' +
    'If your backend is on a different domain, please set PRODUCTION_API_URL in src/utils/apiConfig.ts'
  );
  return window.location.origin;
};

// Export the API base URL
export const API_BASE_URL = getApiUrl();

/**
 * Helper function to build API endpoint URLs
 * @param endpoint - API endpoint path (e.g., '/api/chat' or 'api/chat')
 * @returns Full URL to the endpoint
 */
export const getApiEndpoint = (endpoint: string): string => {
  const baseUrl = API_BASE_URL.endsWith('/') ? API_BASE_URL.slice(0, -1) : API_BASE_URL;
  const path = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  return `${baseUrl}${path}`;
};

