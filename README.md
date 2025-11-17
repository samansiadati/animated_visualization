<title>CO₂ Emissions Visualization Project</title>
<style>
    /* Import Google Font for modern look */
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap');

    body {
        font-family: 'Roboto', sans-serif;
        line-height: 1.7;
        margin: 0;
        padding: 0;
        background: #f4f6f8;
        color: #2c3e50;
    }

    header {
        background: linear-gradient(90deg, #4D79FF, #2ECC71);
        color: white;
        padding: 3rem 1rem;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
        letter-spacing: 1px;
    }

    header p {
        margin: 0.5rem 0 0;
        font-size: 1.2rem;
        font-weight: 400;
        font-style: italic;
        opacity: 0.9;
    }

    main {
        max-width: 1000px;
        margin: -50px auto 2rem;
        padding: 2rem;
    }

    section {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        transition: transform 0.3s;
    }

    section:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
    }

    h2 {
        color: #4D79FF;
        margin-bottom: 1rem;
        font-size: 1.8rem;
        border-bottom: 2px solid #2ECC71;
        display: inline-block;
        padding-bottom: 5px;
    }

    h3 {
        color: #FF6B6B;
        margin-top: 1.2rem;
        margin-bottom: 0.5rem;
        font-size: 1.4rem;
    }

    p {
        margin-bottom: 1rem;
        font-size: 1rem;
    }

    code, pre {
        font-family: 'Courier New', monospace;
        background: #f1f3f6;
        padding: 0.2rem 0.5rem;
        border-radius: 6px;
        overflow-x: auto;
    }

    pre {
        padding: 1rem;
        margin-bottom: 1rem;
    }

    a {
        color: #4D79FF;
        text-decoration: none;
        font-weight: 500;
    }

    a:hover {
        text-decoration: underline;
    }

    ul {
        margin: 0.5rem 0 0.5rem 1.5rem;
    }

    img {
        max-width: 100%;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        transition: transform 0.3s;
    }

    img:hover {
        transform: scale(1.03);
    }

    footer {
        text-align: center;
        padding: 1.5rem;
        font-size: 0.9rem;
        color: #7f8c8d;
    }
</style>
