Total_land = 80
Segments = 5
Acres_per_segment = Total_land / Segments
# --- 1. Tomato Sales ---
tomato_acres = Acres_per_segments
tomato_30_segment = 0.30 * tomato_acres
tomato_70_segment = 0.70 * tomato_acres

# Conversion: tonnes to kg (* 1000), price is Rs. 7 per kg
tomato_yield_kg = (tomato_30_segment * 10 * 1000) + (tomato_70_segment * 12 * 1000)
tomato_sales = tomato_yield_kg * 7

# --- 2. Potato Sales ---
# Yield: 10 tonnes per acre. Price: Rs. 20 per kg
potato_yield_kg = Acres_per_segments * 10 * 1000
potato_sales = potato_yield_kg * 20

# --- 3. Cabbage Sales ---
# Yield: 14 tonnes per acre. Price: Rs. 24 per kg
cabbage_yield_kg = Acres_per_segments * 14 * 1000
cabbage_sales = cabbage_yield_kg * 24

# --- 4. Sunflower Sales ---
# Yield: 0.7 tonnes per acre. Price: Rs. 200 per kg
sunflower_yield_kg = Acres_per_segments * 0.7 * 1000
sunflower_sales = sunflower_yield_kg * 200

# --- 5. Sugarcane Sales ---
# Yield: 45 tonnes per acre. Price: Rs. 4,000 per TONNE
sugarcane_yield_tonnes = Acres_per_segments * 45
sugarcane_sales = sugarcane_yield_tonnes * 4000

# Total 
total_overall_sales = (tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales
)