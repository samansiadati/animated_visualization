import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import imageio
import os

# -------------------------------
# 1. Load Kaggle CSV dataset
# -------------------------------
csv_path = "~/projects/iitech/data_viz/mod5/data/GCB2022v27_MtCO2_flat.csv"  # Update path as needed
df_raw = pd.read_csv(csv_path)



# -------------------------------
# 2. Filter major countries and meaningful years
# -------------------------------
countries = ["United States", "China", "India"]
df = df_raw[df_raw["Country"].isin(countries)].copy()

# Keep years >= 1950 to avoid early zeros
df = df[df["Year"] >= 1950]

# Ensure Year is int and sort
df["Year"] = df["Year"].astype(int)
df = df.sort_values(["Country", "Year"])

# -------------------------------
# 3. Plotly interactive HTML
# -------------------------------
fig = px.line(
    df,
    x="Year",
    y="Total",
    color="Country",
    title="Global Fossil CO₂ Emissions Over Time (1950–2022)<br><sup>Major emitters: US, China, India</sup>",
    animation_frame="Year",
    range_y=[0, df["Total"].max() * 1.1],
    color_discrete_sequence=["#FF6B6B", "#4D79FF", "#2ECC71"]
)

fig.update_layout(
    template="plotly_white",
    title_font_size=24,
    legend_title_text="Country",
    yaxis_title="CO₂ Emissions (MtCO₂)"
)

html_path = "co2_emissions_kaggle.html"
fig.write_html(html_path)
print(f"Interactive HTML saved to: {html_path}")

# -------------------------------
# 4. GIF animation
# -------------------------------
gif_path = "co2_emissions_kaggle.gif"
frame_dir = "frames_kaggle"
os.makedirs(frame_dir, exist_ok=True)

years = sorted(df["Year"].unique())
images = []

for year in years:
    plt.figure(figsize=(10, 5))
    
    for country, color in zip(countries, ["#FF6B6B", "#4D79FF", "#2ECC71"]):
        subset = df[(df["Country"] == country) & (df["Year"] <= year)]
        if len(subset) > 0:
            plt.plot(subset["Year"], subset["Total"], color=color, linewidth=2, label=country)
    
    plt.title(f"CO₂ Emissions Over Time – Year: {year}", fontsize=16)
    plt.xlabel("Year")
    plt.ylabel("CO₂ Emissions (MtCO₂)")
    plt.ylim(0, df["Total"].max() * 1.1)
    plt.legend()
    plt.grid(alpha=0.3)

    frame_file = f"{frame_dir}/frame_{year}.png"
    plt.savefig(frame_file, dpi=120)
    plt.close()
    images.append(imageio.imread(frame_file))

imageio.mimsave(gif_path, images, fps=5)
print(f"GIF saved to: {gif_path}")
