# Chapter 2: Energy Efficiency in Thermal Utilities and Systems (CO-4)

## Furnace Fuel Economy Measures

**Q: Enlist various energy conservation techniques for industrial furnaces. (3 marks)**

1. Complete combustion with minimum excess air
2. Correct amount of air for combustion
3. Preheating combustion air using waste heat from flue gases
4. Preheating the charge or load material before placing in furnace
5. Proper insulation and refractory maintenance to reduce wall losses
6. Waste heat recovery from flue gases
7. Controlling furnace draft properly
8. Regular maintenance and calibration of burners

**Q: Write recommendations for efficient design of furnace. (4 marks)**

1. Complete combustion with minimum excess air. Excess air beyond what is needed carries away heat.
2. Preheating combustion air. Using recuperators to preheat air with flue gas heat saves about 1% fuel for every 20°C rise.
3. Preheating the charge. Preheating materials using waste flue gases directly reduces the energy needed to reach operating temperatures.
4. Proper insulation. Using ceramic fiber insulation on furnace walls and doors reduces heat leakage.
5. Controlling furnace draft. Proper draft control prevents air infiltration and incomplete combustion.
6. Waste heat recovery. Use waste heat boilers or regenerators to recover heat from hot flue gases.
7. Efficient burner operation. Ensure regular maintenance and clean nozzles for proper air to fuel ratios.

**Q: Discuss general fuel economy measures in furnaces. (7 marks)**

1. Complete combustion with minimum excess air: Excess air beyond what is needed for complete combustion carries away heat. Typical excess air should be 10 to 25% depending on fuel type. Monitor O2 in flue gas.
2. Preheating combustion air: For every 20°C rise in combustion air temperature, fuel savings of about 1% can be achieved. Use recuperators or regenerators to preheat air using flue gas heat.
3. Preheating the charge: If the charge is preheated using waste flue gases, the furnace needs less energy to bring it to operating temperature. This directly reduces fuel consumption.
4. Controlling furnace draft: Excessive draft increases air infiltration and heat loss. Insufficient draft causes incomplete combustion. Use dampers and draft gauges.
5. Proper insulation: Use ceramic fiber insulation on furnace walls and doors. Every crack or opening leaks heat. Maintain refractory lining regularly.
6. Waste heat recovery from flue gases: Use recuperators, regenerators, or waste heat boilers to recover heat from hot flue gases. Flue gas temperature above 750°C has significant recoverable heat.
7. Optimum temperature control: Avoid overheating. Every 10°C rise above required temperature increases fuel consumption by about 1 to 2%.
8. Reducing heat stored in furnace structure: Use low thermal mass materials like ceramic fiber instead of firebrick for furnace walls. This reduces heat stored in walls during heating cycles.
9. Minimizing wall losses: Reduce openings, use properly sized doors, and keep doors closed when not loading or unloading.
10. Efficient burner operation: Ensure regular maintenance, proper air to fuel ratio, and clean nozzles.

## Boilers: Efficiency Evaluation

**Q: Define boiler efficiency. Explain direct and indirect methods of boiler efficiency evaluation. (3 marks / 4 marks)**

Boiler efficiency is the ratio of heat output (heat absorbed by steam) to heat input (heat content of fuel fired).

Evaporation Ratio is the ratio of steam generated per kg of fuel consumed. ER = Steam generation (kg/hr) / Fuel consumption (kg/hr). Typical values are 4 to 8 for coal and 12 to 14 for oil.

Direct Method (Input-Output Method):
Formula: η = [Q × (hs - hfw)] / [q × GCV] × 100
where Q = steam generation rate (kg/hr), hs = enthalpy of steam (kcal/kg), hfw = enthalpy of feed water (kcal/kg), q = fuel firing rate (kg/hr), GCV = Gross Calorific Value of fuel (kcal/kg).
Advantages: Quick, easy, requires few measurements.
Disadvantages: Does not tell you where the losses are, less accurate.

Indirect Method (Heat Loss Method):
Calculates all individual heat losses and subtracts from 100%.
Formula: η = 100 - (sum of all percentage heat losses)
Losses calculated: L1 (dry flue gas), L2 (hydrogen in fuel), L3 (moisture in fuel), L4 (moisture in air), L5 (CO loss), L6 (radiation and unaccounted), L7 (unburnt in fly ash), L8 (unburnt in bottom ash).
Advantages: Tells exactly where losses occur, helps identify improvement areas.
Disadvantages: Requires many measurements, time consuming.

## Boilers: Efficiency Numerical (Indirect Method)

**Q: Calculate the efficiency of a boiler using indirect method for the following data. (7 marks)**

General Formulas:
Theoretical air = [11.6C + 34.8(H2 - O2/8) + 4.35S] / 100 kg/kg of fuel
% Excess Air = O2% / (21 - O2%) × 100
Actual air = Theoretical air × (1 + EA/100)

Given Data:
Ultimate Analysis: Carbon = 84%, Hydrogen = 12%, Nitrogen = 0.5%, Oxygen = 1.5%, Sulphur = 1.5%, Moisture = 0.5%
GCV of fuel = 10000 kcal/kg
Fuel firing rate = 2648.125 kg/hr
Surface temperature of boiler = 90°C
Humidity = 0.025 kg/kg of dry air
Theoretical air required = 13.92 kg/kg of oil
Mass of dry flue gas = 21.36 kg/kg of oil
Flue gas temperature = 190°C
Ambient temperature = 30°C
CO2% in flue gas = 10.8%
O2% in flue gas = 7.4%
Cp of flue gas = 0.23 kcal/kg°C
Cp of superheated steam or moisture = 0.45 kcal/kg°C

Solution:

Step 1: Calculate Excess Air
% Excess Air = (O2%) / (21 - O2%) × 100
% Excess Air = 7.4 / (21 - 7.4) × 100
% Excess Air = 7.4 / 13.6 × 100
% Excess Air = 54.41%

Step 2: Calculate Actual Air Supplied
Actual mass of air supplied = Theoretical air × (1 + EA/100)
Actual mass of air supplied = 13.92 × (1 + 54.41/100)
Actual mass of air supplied = 13.92 × 1.5441
Actual mass of air supplied = 21.49 kg/kg of fuel

Step 3: Calculate Individual Losses

L1 = Heat loss due to dry flue gas
L1 = m_dfg × Cp × (Tf - Ta) / GCV × 100
L1 = 21.36 × 0.23 × (190 - 30) / 10000 × 100
L1 = 21.36 × 0.23 × 160 / 10000 × 100
L1 = 785.088 / 10000 × 100
L1 = 7.85%

L2 = Heat loss due to hydrogen in fuel
L2 = 9 × H2 × [584 + Cp_water × (Tf - Ta)] / GCV × 100
L2 = 9 × 0.12 × [584 + 0.45 × (190 - 30)] / 10000 × 100
L2 = 1.08 × [584 + 72] / 10000 × 100
L2 = 1.08 × 656 / 10000 × 100
L2 = 708.48 / 10000 × 100
L2 = 7.08%

L3 = Heat loss due to moisture in fuel
L3 = M × [584 + Cp_water × (Tf - Ta)] / GCV × 100
L3 = 0.005 × [584 + 0.45 × 160] / 10000 × 100
L3 = 0.005 × 656 / 10000 × 100
L3 = 3.28 / 10000 × 100
L3 = 0.03%

L4 = Heat loss due to moisture in air
L4 = AAS × humidity × Cp_water × (Tf - Ta) / GCV × 100
L4 = 21.49 × 0.025 × 0.45 × 160 / 10000 × 100
L4 = 38.682 / 10000 × 100
L4 = 0.39%

L5 = Heat loss due to CO
Since CO is not given in the problem, assume L5 = 0%
If CO is given, L5 = [CO / (CO + CO2)] × C × 5654 / GCV × 100

L6 = Radiation and other unaccounted losses
Assume L6 = 2.0%

Step 4: Calculate Total Losses
Total losses = L1 + L2 + L3 + L4 + L5 + L6
Total losses = 7.85 + 7.08 + 0.03 + 0.39 + 0 + 2.0
Total losses = 17.35%

Step 5: Calculate Boiler Efficiency
Boiler efficiency = 100 - Total losses
Boiler efficiency = 100 - 17.35
Boiler efficiency = 82.65%

## Steam Traps

**Q: What are steam traps? State their functions and benefits. (4 marks)**

Definition: A steam trap is an automatic valve that discharges condensate, air, and non-condensable gases from a steam system while preventing the escape of live steam.

Functions:
1. Remove condensate from steam lines and equipment as soon as it forms.
2. Remove air and non-condensable gases from the steam system.
3. Prevent live steam from escaping to conserve steam.

Benefits:
1. Increases heat transfer efficiency because a condensate film on a heat transfer surface acts as an insulator.
2. Prevents water hammer caused by slugs of condensate in steam lines.
3. Reduces corrosion caused by air and CO2 in the steam system.
4. Saves energy by preventing steam loss.
5. Protects equipment from damage due to condensate accumulation.

**Q: List out types of steam traps and explain any two with neat sketches. (7 marks)**

Definition: A steam trap is an automatic valve that discharges condensate, air, and non-condensable gases from a steam system while preventing the escape of live steam.

Functions:
1. Remove condensate from steam lines and equipment as soon as it forms.
2. Remove air and non-condensable gases from the steam system.
3. Prevent live steam from escaping to conserve steam.

Benefits:
1. Increases heat transfer efficiency.
2. Prevents water hammer.
3. Reduces corrosion.
4. Saves energy by preventing steam loss.
5. Protects equipment from damage.

Types of Steam Traps:
1. Mechanical traps work on the density difference between steam and condensate. Examples include the ball float trap and inverted bucket trap.
2. Thermostatic traps work on the temperature difference between steam and condensate. Examples include the balanced pressure trap and bimetallic trap.
3. Thermodynamic traps work on the difference in flow characteristics of steam and condensate. Examples include the disc trap.

Explain Ball Float Trap:
A hollow ball floats on condensate and sinks in steam. When condensate enters the trap body, the float rises and opens the valve, allowing condensate to drain. When steam enters, the float drops and closes the valve, trapping the steam. This trap gives continuous condensate discharge.
[DIAGRAM: Ball float steam trap showing inlet, float ball, valve seat, outlet, and body]

Explain Inverted Bucket Trap:
An inverted bucket inside the trap body floats when steam enters it due to buoyancy. When steam enters the bucket, it floats up and closes the outlet valve. As steam condenses inside the bucket, the bucket sinks and opens the valve to discharge condensate. This trap operates intermittently.
[DIAGRAM: Inverted bucket steam trap showing inverted bucket, inlet, outlet valve, and body]

## Energy Conservation in Refrigeration and Air Conditioning

**Q: List factors affecting refrigeration and air conditioning system performance and explain any one. Explain techniques of energy conservation in refrigerated cold storage plants. (4 marks)**

Factors affecting system performance:
1. Evaporator temperature and condition. Fouled coils reduce performance.
2. Condenser temperature and condition. A dirty condenser increases head pressure.
3. Refrigerant charge. Undercharge or overcharge both reduce COP.
4. Compressor efficiency and capacity control.
5. Insulation of cold rooms and chilled water pipes.
6. Air infiltration through doors and loading docks.
7. Heat load from lighting, people, and equipment inside the conditioned space.

Explain condenser condition:
If the condenser coils are dirty or fouled, heat rejection is poor. This increases the condensing pressure and temperature. For every 1°C increase in condensing temperature, power consumption of the compressor increases by about 3 to 3.5%. Regular cleaning of condenser coils can save 5 to 10% of energy.

**Q: List the energy saving opportunities in refrigeration and air conditioning plant. (7 marks)**

1. Maintain proper condenser cleaning schedule. Dirty condensers increase compressor power by 3% per degree rise in condensing temperature.
2. Increase evaporator temperature. For every 1°C increase in evaporator temperature, COP improves by 2 to 3%. Do not cool below the required temperature.
3. Ensure proper refrigerant charge. Both undercharge and overcharge reduce efficiency.
4. Use variable frequency drives (VFDs) on compressors and fans for part-load operation.
5. Reduce air infiltration in cold rooms. Install strip curtains, air curtains, or rapid-closing doors.
6. Improve insulation on cold room walls, floors, and ceilings. Check for damaged insulation.
7. Reduce internal heat loads. Use LED lighting inside cold rooms instead of incandescent. Minimize door opening frequency.
8. Regular maintenance of expansion valves, filters, and oil levels.
9. Use economizer cycle or free cooling when ambient temperature is low enough.
10. Recover condenser waste heat for water heating or space heating.
11. Group similar temperature products together. Avoid mixing products with different temperature requirements.
12. Proper sizing of equipment. Oversized systems cycle on and off frequently, wasting energy.

## Blow Down

**Q: Explain blow down, its necessity, and advantages. (4 marks)**

Blow down is the process of removing a portion of boiler water from the drum to reduce the concentration of dissolved solids, chemicals, and other impurities.

Necessity:
As water evaporates into steam in the boiler, dissolved solids remain behind and their concentration keeps increasing. If not removed, these concentrated impurities cause scale formation on heat transfer surfaces, foaming and carryover of water into steam, and corrosion of boiler tubes. Blow down keeps the total dissolved solids (TDS) within acceptable limits.

Types:
1. Intermittent blow down or bottom blow down. Done manually at intervals. Removes sludge and heavy sediment from the bottom of the boiler drum. Takes about 10 to 15 seconds each time.
2. Continuous blow down. Water is continuously removed from the point of highest TDS concentration. Flow rate is controlled by a valve. Allows heat recovery from blow down water.

Advantages:
1. Prevents scale formation on boiler tubes. Scale even 1mm thick can increase fuel consumption by 5 to 8%.
2. Reduces foaming and carryover of water droplets in steam.
3. Prevents corrosion of boiler tubes and drum.
4. Maintains water quality within prescribed limits.
5. Continuous blow down heat can be recovered using a flash tank and heat exchanger.

## Energy Conservation Opportunities for Boilers

**Q: Discuss the energy conservation opportunities for boiler in detail. (7 marks)**

1. Reduce excess air: Monitor and control excess air using O2 analyzers. For every 1% reduction in excess air, fuel savings of about 0.5% can be achieved. Typical excess air is 15 to 20% for oil and 20 to 30% for coal.
2. Install economizer: Recovers heat from flue gases to preheat boiler feed water. For every 6°C increase in feed water temperature, fuel savings of about 1% can be achieved.
3. Install air preheater: Uses flue gas heat to preheat combustion air. For every 20°C rise in combustion air temperature, there is about 1% fuel saving.
4. Minimize blow down: Excessive blow down wastes energy. Use automatic TDS controllers. Recover heat from blow down water using flash tanks.
5. Improve boiler insulation: Check and repair damaged insulation on boiler shell, steam pipes, and valves. A bare steam pipe at 200°C can lose 1000 kcal/hr per meter length.
6. Recover condensate: Return hot condensate to the boiler feed water tank. Condensate at 90°C contains about 50 kcal/kg of heat that would otherwise be wasted.
7. Optimize boiler loading: Operate boiler at 65 to 85% of rated capacity for best efficiency. Very low loads below 25% and overloading both reduce efficiency.
8. Improve feed water treatment: Scale on boiler tubes acts as an insulator. Even 1mm of calcium scale can increase fuel consumption by 5 to 8%. Proper softening and deaeration of feed water prevents scale.
9. Reduce steam leaks: A small leak of 3mm diameter on a 7 kg/cm2 steam line can waste about 30 tons of steam per year.
10. Use waste heat from flue gases: If flue gas exit temperature is above 200°C, there is significant scope for heat recovery.
11. Regular soot blowing: Soot deposits on boiler tubes act as an insulator and reduce heat transfer. Regular soot blowing maintains heat transfer efficiency.
12. Monitor and maintain steam traps: Failed steam traps can cause significant steam and condensate losses.

## Losses in Fuel-Fired Furnaces

**Q: Discuss various losses in fuel-fired furnaces in detail. (7 marks)**

1. Heat loss through flue gases or stack loss: This is the largest loss, typically 30 to 40% of total heat input. Hot flue gases carry away sensible heat. Loss depends on flue gas temperature and excess air. Higher flue gas temperature results in higher loss. In a well-designed furnace, this should be minimized to 20 to 25%.
2. Heat loss due to incomplete combustion: If combustion is incomplete, CO is formed instead of CO2. CO has a calorific value of 2400 kcal/Nm3 that is wasted. This is caused by insufficient air, poor mixing, or low combustion temperature.
3. Heat loss through furnace walls or wall loss: Heat is conducted through furnace walls and radiated from outer surfaces. This depends on insulation thickness, wall temperature, and furnace surface area. Typically 2 to 5% of total input.
4. Heat loss due to opening in furnace: Every time the furnace door opens, hot gases escape and cold air enters. Radiation heat loss through openings is proportional to the fourth power of temperature. Keep doors closed and properly sealed.
5. Heat stored in furnace structure: During heating, the furnace walls, hearth, and roof absorb heat. This is a loss during batch operations because stored heat is wasted during the cooling period. Use low thermal mass materials like ceramic fiber to reduce this loss.
6. Heat loss due to water cooling: In furnaces with water-cooled components like doors, frames, and skid pipes, heat is removed by cooling water. This heat is usually not recovered.
7. Heat loss due to scale formation: Oxidation of the metal surface forms scale. Scale formation represents material loss and the heat absorbed by the oxidation process.
8. Heat carried away by the heated material or useful heat: This is not actually a loss, it is the useful output. However, if the product is overheated beyond requirement, the extra heat is wasted.

## Feed Water Treatment and Deaeration

**Q: Explain deaeration treatment for boiler water. (3 marks)**

Deaeration is the process of removing dissolved gases, mainly oxygen and carbon dioxide, from boiler feed water before it enters the boiler.

Why it is needed:
Dissolved oxygen causes pitting corrosion on boiler tubes and drum. CO2 forms carbonic acid which causes acidic corrosion. Even small amounts like 0.1 ppm of O2 can cause significant damage over time.

How it works:
Feed water is heated to its saturation temperature in a deaerator vessel. At saturation temperature, the solubility of gases in water drops to near zero, and dissolved gases are released. These gases are vented out through a vent condenser at the top of the deaerator. The deaerator also acts as a feed water heater, raising the water temperature to 105 to 110°C.

Types:
1. Spray type deaerator.
2. Tray type deaerator.
