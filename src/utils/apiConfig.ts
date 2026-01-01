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
// IMPORTANT: This should be your BACKEND URL, not your frontend URL!
// Vercel typically hosts frontends, not Python FastAPI backends.
// Your backend should be deployed on Railway, Render, or similar.
//
// Examples:
// - Railway: 'https://your-backend-app.railway.app'
// - Render: 'https://your-backend-app.onrender.com'
// - Fly.io: 'https://your-backend-app.fly.dev'
// - Custom: 'https://api.yourdomain.com'
//
// To find your backend URL:
// 1. Check your Railway/Render dashboard
// 2. Test it: curl https://your-backend-url/api/health
// 3. It should return: {"status":"healthy","service":"robotics-book-rag"}
//
// Leave empty to use same origin (only works if backend is on same domain)
const PRODUCTION_API_URL = 'https://hackathon-book-documnetation.vercel.app/'; // <-- UPDATE THIS with your actual BACKEND URL

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

// Log the API URL in development for debugging
if (typeof window !== 'undefined' && window.location.hostname !== 'localhost') {
  console.log('API Base URL:', API_BASE_URL);
}

/**
 * Helper function to build API endpoint URLs
 * @param endpoint - API endpoint path (e.g., '/api/chat' or 'api/chat')
 * @returns Full URL to the endpoint
 */
export const getApiEndpoint = (endpoint: string): string => {
  const baseUrl = API_BASE_URL.endsWith('/') ? API_BASE_URL.slice(0, -1) : API_BASE_URL;
  const path = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  const fullUrl = `${baseUrl}${path}`;
  
  // Log in development for debugging
  if (typeof window !== 'undefined' && window.location.hostname === 'localhost') {
    console.log(`API Endpoint: ${fullUrl}`);
  }
  
  return fullUrl;
};

