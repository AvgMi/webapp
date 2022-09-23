mkdir -p ~/.streamlit/
echo "\
[general]\n\
email = \"golharakshay9@gmail.com\"\n\
"> ~/.stramlit/credentials.toml
echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
"> ~/.streamlit/config.toml
