// LawFlake Configuration
// Use production API URL or fallback to localhost for development
const API_BASE_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://127.0.0.1:8000/api/v1'
    : 'https://lawflake-production.up.railway.app/api/v1';

// Export globally (IMPORTANTE!)
window.API_BASE_URL = API_BASE_URL;
window.API_URL = API_BASE_URL;

const config = {
    apiUrl: API_BASE_URL,
    supabaseUrl: 'https://bydfdmmyzjdsfaomhwse.supabase.co',
    supabaseKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJ5ZGZkbW15empkc2Zhb21od3NlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjExMzA2MTIsImV4cCI6MjA3NjcwNjYxMn0.J1Ju2irp4qSPZWM4HwY8ZcIMo7kW6qchSGoa3XNShIE'
};
