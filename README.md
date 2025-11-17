<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CO₂ Emissions Visualization Project</title>
<style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 0;
        background-color: #f9f9f9;
        color: #333;
    }
    header {
        background-color: #2ECC71;
        color: white;
        padding: 2rem 1rem;
        text-align: center;
    }
    header h1 {
        margin: 0;
        font-size: 2.2rem;
    }
    header p {
        margin: 0.5rem 0 0;
        font-size: 1.1rem;
        font-style: italic;
    }
    main {
        max-width: 900px;
        margin: 2rem auto;
        padding: 0 1rem;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    section {
        padding: 1.5rem 0;
        border-bottom: 1px solid #eee;
    }
    section:last-child {
        border-bottom: none;
    }
    h2 {
        color: #4D79FF;
        margin-bottom: 0.8rem;
    }
    h3 {
        color: #FF6B6B;
        margin-bottom: 0.5rem;
    }
    code {
        background-color: #eee;
        padding: 2px 5px;
        border-radius: 4px;
        font-family: Consolas, monospace;
    }
    pre {
        background-color: #eee;
        padding: 1rem;
        border-radius: 6px;
        overflow-x: auto;
    }
    a {
        color: #2ECC71;
        text-decoration: none;
    }
    a:hover {
        text-decoration: underline;
    }
    ul {
        margin: 0.5rem 0 0.5rem 1.2rem;
    }
    img {
        max-width: 100%;
        border-radius: 8px;
        margin-top: 0.5rem;
    }
</style>
</head>
<body>

<header>
    <h1>🌍 CO₂ Emissions Visualization Project</h1>
    <p>Interactive & animated visualizations of global fossil CO₂ emissions (1950–2022)</p>
</header>

<main>

<section>
    <h2>Overview</h2>
    <p>This project visualizes global fossil CO₂ emissions over time using both <strong>interactive Plotly charts</strong> and <strong>animated GIFs</strong>. The goal is to tell a clear story of major emitters (US, China, India) and highlight trends and changes over the last decades.</p>
</section>

<section>
    <h2>Dataset</h2>
    <p>We used the following dataset:</p>
    <ul>
        <li><strong>Source:</strong> <a href="https://www.kaggle.com/datasets/thedevastator/global-fossil-co2-emissions-by-country-2002-2022?utm_source=chatgpt.com" target="_blank">Kaggle – Global Fossil CO₂ Emissions by Country (2002–2022)</a></li>
        <li><strong>CSV filename:</strong> <code>GCB2022v27_MtCO2_flat.csv</code></li>
        <li><strong>Key columns:</strong> <code>Country</code>, <code>ISO 3166-1 alpha-3</code>, <code>Year</code>, <code>Total</code>, <code>Coal</code>, <code>Oil</code>, <code>Gas</code>, <code>Cement</code>, <code>Flaring</code>, <code>Other</code>, <code>Per Capita</code></li>
    </ul>
</section>

<section>
    <h2>Visualizations</h2>
    <h3>1. Interactive Plotly Chart</h3>
    <p>This chart allows users to:</p>
    <ul>
        <li>Hover over lines to see exact CO₂ emissions.</li>
        <li>Watch emissions grow dynamically year by year.</li>
        <li>Compare trends for US, China, and India.</li>
    </ul>
    <p>Saved as <code>co2_emissions_kaggle.html</code></p>
    <img src="co2_emissions_kaggle_screenshot.png" alt="Plotly Interactive Chart Screenshot">
    
    <h3>2. Animated GIF</h3>
    <p>The GIF shows year-by-year growth of emissions for the same countries:</p>
    <ul>
        <li>Lines grow over time to show trends clearly.</li>
        <li>Filtered from 1950 onwards to avoid early zeros.</li>
    </ul>
    <p>Saved as <code>co2_emissions_kaggle.gif</code></p>
    <img src="co2_emissions_kaggle.gif" alt="CO2 Emissions GIF">
</section>

<section>
    <h2>Setup Instructions</h2>
    <pre><code>pip install pandas plotly matplotlib imageio
python main.py</code></pre>
    <p>Make sure the CSV file is located in the <code>data/</code> folder.</p>
</section>

<section>
    <h2>Customization</h2>
    <ul>
        <li>Change displayed countries by editing the <code>countries</code> list in <code>main.py</code>.</li>
        <li>Adjust year range by editing the filter: <code>df = df[df["Year"] >= 1950]</code></li>
        <li>Change colors using Plotly's <code>color_discrete_sequence</code>.</li>
    </ul>
</section>

<section>
    <h2>Key Insights</h2>
    <ul>
        <li>CO₂ emissions of major countries have dramatically increased since 1950.</li>
        <li>China surpasses other countries in the 2000s.</li>
        <li>The visualization provides a clear, intuitive view for educators, policymakers, and general audiences.</li>
    </ul>
</section>

<section>
    <h2>Acknowledgments</h2>
    <ul>
        <li>Dataset from <a href="https://www.kaggle.com/datasets/thedevastator/global-fossil-co2-emissions-by-country-2002-2022?utm_source=chatgpt.com" target="_blank">Kaggle</a></li>
        <li>Developed with Python, Plotly, Matplotlib, and ImageIO</li>
    </ul>
</section>

<section>
    <h2>License</h2>
    <p>This project is for educational purposes. Dataset is under Kaggle terms.</p>
</section>

</main>

</body>
</html>
