// API utilities (COPIADO DO PRDMANAGER)
const API_URL = window.API_BASE_URL || 'http://127.0.0.1:8000/api/v1';

async function apiGet(endpoint) {
    const startTime = performance.now();
    const url = `${API_URL}${endpoint}`;

    console.log(`🌐 API GET ${url}`);

    try {
        const response = await fetch(url, {
            headers: {
                'Authorization': `Bearer ${getToken()}`
            }
        });

        const duration = performance.now() - startTime;
        const data = await response.json();

        if (!response.ok) {
            console.error(`❌ API GET ${url} - ${response.status} - ${duration.toFixed(2)}ms`, data);

            if (response.status === 401) {
                console.log('🚪 401 Unauthorized - Clearing session...');
                localStorage.clear();
                window.location.href = 'login.html';
                return;
            }

            throw new Error(data.detail || data.message || response.statusText);
        }

        console.log(`✅ API GET ${url} - 200 - ${duration.toFixed(2)}ms`);
        return data;
    } catch (error) {
        console.error(`❌ API GET ${url} - FAILED`, error);
        throw error;
    }
}

async function apiPost(endpoint, data) {
    const startTime = performance.now();
    const url = `${API_URL}${endpoint}`;

    console.log(`🌐 API POST ${url}`, data);

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${getToken()}`
            },
            body: JSON.stringify(data)
        });

        const duration = performance.now() - startTime;
        const responseData = await response.json();

        if (!response.ok) {
            console.error(`❌ API POST ${url} - ${response.status}`, responseData);

            if (response.status === 401) {
                console.log('🚪 401 Unauthorized - Clearing session...');
                localStorage.clear();
                window.location.href = 'login.html';
                return;
            }

            throw new Error(responseData.detail || responseData.message || response.statusText);
        }

        console.log(`✅ API POST ${url} - ${response.status} - ${duration.toFixed(2)}ms`);
        return responseData;
    } catch (error) {
        console.error(`❌ API POST ${url} - FAILED`, error);
        throw error;
    }
}

async function apiPut(endpoint, data) {
    const response = await fetch(`${API_URL}${endpoint}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getToken()}`
        },
        body: JSON.stringify(data)
    });

    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || response.statusText);
    }

    return await response.json();
}

async function apiDelete(endpoint) {
    const response = await fetch(`${API_URL}${endpoint}`, {
        method: 'DELETE',
        headers: {
            'Authorization': `Bearer ${getToken()}`
        }
    });

    if (!response.ok) {
        const error = await response.json();
        throw new Error(error.detail || response.statusText);
    }

    return await response.json();
}
