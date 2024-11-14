import math

# Constants (assuming historical conditions similar to Nagasaki)
yld = 21  # kilotonn; TNT ma
dens_core = 1322   # people per km^2 in central Kirtipur
dens_outskirts = 893  # kirtipur oripari ko pop. density l
valley_amplification = 1.5  # estimated factor for constructive interference, valley vitra matra
#population teti bela ko (hisab garera nikaleko ho on the basis of 2021 ko census and annual pop.growth) = 19,513

#I evperimented with yo values haru, ani tala ko data chai I was convinced. Visitor can play with the various constraints. 

fireball_rad = 0.2  # km
total_dest_rad = 1.5  # km
severe_dmg_rad = 3.0  # km, increased to account for valley amplification
moderate_dmg_rad = 5.0  # km

# Calculate shockwave decay with distance (inverse square law for energy spread ko principle)
#Esko theory arko file ma chha, If I wish to check one for myself
def shockwave_intensity(distance, amplification=1.0):
    return amplification / (distance ** 2)

# Estimate casualties based on radius and population density
def est_casualties(radius, density, amplification_factor=1.0):
    area = math.pi * (radius ** 2)
    pop = area * density
    # amplified shockwave
    effective_pop = pop * shockwave_intensity(radius, amplification_factor)
    return effective_pop

# casualties ko sankhya in each zone 
fireball_casualties = est_casualties(fireball_rad, dens_core, valley_amplification)
total_dest_casualties = est_casualties(total_dest_rad, dens_core, valley_amplification)
severe_dmg_casualties = est_casualties(severe_dmg_rad, dens_outskirts, valley_amplification)
moderate_dmg_casualties = est_casualties(moderate_dmg_rad, dens_outskirts, valley_amplification)

# Total estimated casualties
total_casualties = fireball_casualties + total_dest_casualties + severe_dmg_casualties + moderate_dmg_casualties


print("1945 Kirtipur Nuclear Blast Casualty Estimates (with Valley Shockwave Amplification):")
print(f"Fireball Zone: {fireball_casualties:.0f} casualties")
print(f"Total Destruction Zone: {total_dest_casualties:.0f} casualties")
print(f"Severe Damage Zone: {severe_dmg_casualties:.0f} casualties")
print(f"Moderate Damage Zone: {moderate_dmg_casualties:.0f} casualties")
print(f"Total Estimated Casualties: {total_casualties:.0f}")
