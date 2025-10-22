// Authentication utilities (COPIADO DO PRDMANAGER)

function checkAuth() {
    const token = localStorage.getItem('access_token') || localStorage.getItem('token');

    const publicPages = ['login', 'forgot-password', 'reset-password'];
    const isPublicPage = publicPages.some(page => window.location.pathname.includes(page));

    if (isPublicPage) {
        if (window.location.pathname.includes('login') && token) {
            window.location.href = 'dashboard.html';
            return false;
        }
        return true;
    }

    if (!token) {
        console.log('🔒 No token found, redirecting to login...');
        window.location.href = 'login.html';
        return false;
    }

    // Sync tokens
    if (localStorage.getItem('access_token') && !localStorage.getItem('token')) {
        localStorage.setItem('token', localStorage.getItem('access_token'));
    } else if (localStorage.getItem('token') && !localStorage.getItem('access_token')) {
        localStorage.setItem('access_token', localStorage.getItem('token'));
    }

    console.log('✅ Token found');
    return true;
}

async function logout() {
    try {
        const sessionId = localStorage.getItem('session_id');

        if (sessionId && window.apiPost) {
            await apiPost('/auth/logout', {
                session_id: sessionId,
                revoke_all_devices: false
            });
        }
    } catch (error) {
        console.error('❌ Logout failed:', error);
    } finally {
        localStorage.removeItem('access_token');
        localStorage.removeItem('token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('session_id');
        localStorage.removeItem('token_expires_at');
        localStorage.removeItem('user');

        window.location.href = 'login.html';
    }
}

function getUser() {
    return JSON.parse(localStorage.getItem('user') || '{}');
}

function getToken() {
    return localStorage.getItem('access_token') || localStorage.getItem('token');
}
