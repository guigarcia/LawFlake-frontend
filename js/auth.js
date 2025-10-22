// LawFlake Auth Module
const { createClient } = supabase;

// Initialize Supabase client
const supabaseClient = createClient(config.supabaseUrl, config.supabaseKey);

// Check if user is authenticated
async function checkAuth() {
    const { data: { session } } = await supabaseClient.auth.getSession();

    if (!session && window.location.pathname !== '/public/login.html') {
        window.location.href = 'login.html';
        return null;
    }

    return session;
}

// Login function
async function login(email, password) {
    try {
        const { data, error } = await supabaseClient.auth.signInWithPassword({
            email,
            password
        });

        if (error) throw error;

        return data;
    } catch (error) {
        console.error('Login error:', error);
        throw error;
    }
}

// Logout function
async function logout() {
    await supabaseClient.auth.signOut();
    window.location.href = 'login.html';
}

// Get current user
async function getCurrentUser() {
    const { data: { user } } = await supabaseClient.auth.getUser();
    return user;
}

// Get auth token
async function getAuthToken() {
    const { data: { session } } = await supabaseClient.auth.getSession();
    return session?.access_token;
}
