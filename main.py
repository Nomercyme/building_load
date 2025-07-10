import pandas as pd
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA
from rich.console import Console

console = Console()

console.rule("[bold blue]Step 1: Loading Excel Data")
with console.status("Reading Excel files...", spinner="dots"):
    df = pd.read_excel('data/data_v1.0.xlsx')
    df2 = pd.read_excel('data/data_v2.0.xlsx')

console.log("[green]Loaded both Excel files successfully.")

console.rule("[bold blue]Step 2: Parsing Time Columns")
df['time'] = pd.to_datetime(df['time'], format='%H:%M:%S')
df2['time'] = pd.to_datetime(df2['time'], format='%H:%M:%S')
console.log("[green]Time columns parsed to datetime format.")

console.rule("[bold blue]Step 3: Renaming and Combining DataFrames")
df2 = df2.rename(columns={'temperature (˚C)': 'temperature (ºC)'})
df_combined = pd.concat([df, df2], ignore_index=True)
console.log("[green]DataFrames merged and temperature columns aligned.")

console.rule("[bold blue]Step 4: Creating Continuous Time Index")
df_combined['time'] = pd.date_range(start='1900-01-01', periods=len(df_combined), freq='5min')
console.log("[green]Time column replaced with continuous datetime index.")

console.rule("[bold blue]Step 5: Renaming Columns and Adding ID")
df_combined = df_combined.rename(columns={"time": "ds", "power (W)": "y"})
df_combined["unique_id"] = "building_load"
console.log("[green]Renamed columns and added unique_id.")

console.rule("[bold blue]Step 6: Initializing Forecast Model")
seasonality = 288  # 5-min data → daily seasonality = 24*60 / 5
sf = StatsForecast(
    models=[AutoARIMA(season_length=seasonality)],
    freq='5min',
)
console.log(f"[green]StatsForecast initialized with seasonality={seasonality}.")

console.rule("[bold blue]Step 7: Fitting the Model")
try:
    with console.status("Fitting the model... this might take a moment", spinner="bouncingBar"):
        sf.fit(df_combined)
    console.log("[green]Model fitting complete.")
except Exception as e:
    console.log("[red]❌ An error occurred while fitting the model.")
    console.print_exception()
    raise  # Optionally stop the script completely here

console.rule("[bold blue]Step 8: Making Predictions")
try:
    forecast = sf.predict(h=24, level=[95])
    console.log("[green]Prediction for next 2 hours (24 x 5-min intervals) done.")
except Exception as e:
    console.log("[red]❌ An error occurred while making predictions.")
    console.print_exception()
    raise

console.rule("[bold green]✅ Script Finished Successfully")
