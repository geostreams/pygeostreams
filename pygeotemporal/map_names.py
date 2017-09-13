import copy
import logging


def map_names(input_name, input_option=None):
    # FIXME load mapping from yaml file using csv.py
    output_name = None
    if input_option is not None:
        # IEPA

        if input_name == "Kjeldahl nitrogen":
            if input_option == "Total":
                output_name = "nitrogen-kjeldahl-total-as-n-mgl"
            elif input_option == "Dissolved":
                output_name = "nitrogen-kjeldahl-dissolved-as-n-mgl"
        elif input_name == "Phosphorus":
            if input_option == "Total":
                output_name = "phosphorus-total-as-p-mgl"
            elif input_option == "Dissolved":
                output_name = "phosphorus-dissolved-as-p-mgl"
        elif input_name == "Ammonia-nitrogen":
            if input_option == "Total":
                output_name = "nitrogen-ammonia-total-as-n-mgl"
            elif input_option == "Dissolved":
                output_name = "nitrogen-ammonia-dissolved-as-n-mgl"

        # IEPA ADDED 20161107
        elif input_name == "Inorganic nitrogen (nitrate and nitrite)":
            if input_option == "Total":
                output_name = "nitrate-nitrite-inorganic-total-as-n-mgl"
        elif input_name == "Total suspended solids":
            if input_option == "":
                output_name = "suspended-solids-total-mgl"
        elif input_name == "Volatile suspended solids":
            if input_option == "":
                output_name = "volatile-solids-suspended-mgl"
        elif input_name == "Total volatile solids":
            if input_option == "":
                output_name = "volatile-solids-total-mgl"
        elif input_name == "pH":
            if input_option == "":
                output_name = "pH"
        elif input_name == "Chlorophyll b":
            if input_option == "Total":
                output_name = "chlorophyll-b-ugl"
        elif input_name == "Chlorophyll c":
            if input_option == "Total":
                output_name = "chlorophyll-c-ugl"
        elif input_name == "Chlorophyll a, corrected for pheophytin":
            if input_option == "Total":
                output_name = "chlorophyll-a-corrected-for-pheophytin-ugl"
        elif input_name == "Chlorophyll a, uncorrected for pheophytin":
            if input_option == "Total":
                output_name = "chlorophyll-a-uncorrected-for-pheophytin-ugl"
        elif input_name == "Alkalinity, total":
            if input_option == "":
                output_name = "alkalinity-total-mgl"
        elif input_name == "Nitrate":
            if input_option == "Total":
                output_name = "nitrate-mgl"
        elif input_name == "Nitrite":
            if input_option == "Total":
                output_name = "total-nitrite-mgl"
        else:
            logging.warning(" [map_names] Not able to map input_name " + input_name + " and " + input_option)
            output_name = copy.copy(input_name)

        return output_name

    # GREON
    if input_name[1:len(input_name) - 1] == "YSI_Temp_C":
        output_name = "temperature-c"
    elif input_name[1:len(input_name) - 1] == "YSI_Cond_uScm":
        output_name = "conductivity-uscm"
    elif input_name[1:len(input_name) - 1] == "YSI_SpCond_uScm":
        output_name = "specific-conductivity-uscm"
    elif input_name[1:len(input_name) - 1] == "YSI_Sal_PSU":
        output_name = "salinity-psu"
    elif input_name[1:len(input_name) - 1] == "YSI_ODO_Sat":
        output_name = "dissolved-oxygen-saturation-pct"
    elif input_name[1:len(input_name) - 1] == "YSI_ODO_mgL":
        output_name = "dissolved-oxygen-mgl"
    elif input_name[1:len(input_name) - 1] == "YSI_Turb_FNU":
        output_name = "turbidity-fnu"
    elif input_name[1:len(input_name) - 1] == "YSI_TSS_mgL":
        output_name = "suspended-solids-mgl"
    elif input_name[1:len(input_name) - 1] == "YSI_Chl_RFU":
        output_name = "chlorophyll-rfu"
    elif input_name[1:len(input_name) - 1] == "YSI_Chl_ugL":
        output_name = "chlorophyll-mgl"
    elif input_name[1:len(input_name) - 1] == "YSI_fDOM_RFU":
        output_name = "fine-dissolved-organic-matter-rfu"
    elif input_name[1:len(input_name) - 1] == "YSI_fDOM_QSU":
        output_name = "fine-dissolved-organic-matter-qsu"
    elif input_name[1:len(input_name) - 1] == "YSI_NO3_mgL":
        output_name = "nitrate-mgl"
    elif input_name[1:len(input_name) - 1] == "YSI_NH3_mgL":
        output_name = "ammonia-mgl"
    elif input_name[1:len(input_name) - 1] == "YSI_NH4_mgL":
        output_name = "ammonium-mgl"
    elif input_name[1:len(input_name) - 1] == "PAR_Density_Avg":
        output_name = "par-density-avg"
    elif input_name[1:len(input_name) - 1] == "WindSpd_mph":
        output_name = "wind-speed-mph"
    elif input_name[1:len(input_name) - 1] == "BaroPress_inHg_Avg":
        output_name = "barometric-pressure-24hr-avg-hg"
    elif input_name[1:len(input_name) - 1] == "WindDir":
        output_name = "wind-direction"
    elif input_name[1:len(input_name) - 1] == "RainIn_Tot":
        output_name = "rain-accumulation-24hr-total-inch"
    elif input_name[1:len(input_name) - 1] == "RhPct_Avg":
        output_name = "relative-humidity-24hr-avg"
    elif input_name[1:len(input_name) - 1] == "CompassAve":
        output_name = "compass-heading-24hr-avg"
    elif input_name[1:len(input_name) - 1] == "AirTempF_Avg":
        output_name = "air-temperature-24hr-avg-f"
    elif input_name[1:len(input_name) - 1] == "WindSpd_mph_Max":
        output_name = "wind-speed-24hr-max-mph"
    elif input_name[1:len(input_name) - 1] == "PAR_Raw_mV_Avg":
        output_name = "par-avg-mv"
    elif input_name[1:len(input_name) - 1] == "RECORD":
        output_name = "record"
    elif input_name[1:len(input_name) - 1] == "HailHits_Tot":
        output_name = "hail-hits-total-24hr"
    elif input_name[1:len(input_name) - 1] == "YSI_BGAPC_RFU":
        output_name = "blue-green-algae-pct-rfu"
    elif input_name[1:len(input_name) - 1] == "YSI_BGAPC_ugL":
        output_name = "blue-green-algae-pct-ugl"
    elif input_name[1:len(input_name) - 1] == "Nitrate":
        output_name = "mitrate-mgl"
    elif input_name[1:len(input_name) - 1] == "Ammonia/ Ammonium":
        output_name = "ammonia-ammonium-mgl"
    elif input_name[1:len(input_name) - 1] == "Total Nitrogen":
        output_name = "total-nitrogen-mgl"
    elif input_name[1:len(input_name) - 1] == "Sample Below detection limit":
        output_name = "sample-below-detection-limit"
    elif input_name[1:len(input_name) - 1] == "YSI_Batt_V":
        output_name = "YSI_Batt_V"
    elif input_name[1:len(input_name) - 1] == "SUNA_DarkAve":
        output_name = "SUNA_DarkAve"
    elif input_name[1:len(input_name) - 1] == "SUNA_LightAve":
        output_name = "SUNA_LightAve"
    elif input_name[1:len(input_name) - 1] == "SUNA_Nitrate_uM":
        output_name = "SUNA_Nitrate_uM"
    elif input_name[1:len(input_name) - 1] == "YSI_CablePwr_V":
        output_name = "YSI_CablePwr_V"
    elif input_name[1:len(input_name) - 1] == "YSI_WiperPos_V":
        output_name = "YSI_WiperPos_V"
    elif input_name[1:len(input_name) - 1] == "SUNA_Nitrate_mgL":
        output_name = "SUNA_Nitrate_mgL"

    # USGS
    elif input_name[-5:] == "00010":
        output_name = "water-temperature-c"
    elif input_name[-8:] == "00010_cd":
        output_name = "water-temperature-c-qc"
    elif input_name[-5:] == "00060":
        output_name = "discharge-ft3s"
    elif input_name[-8:] == "00060_cd":
        output_name = "discharge-ft3s-qc"
    elif input_name[-5:] == "00095":
        output_name = "specific-conductance-uScm"
    elif input_name[-8:] == "00095_cd":
        output_name = "specific-conductance-uScm-qc"
    elif input_name[-5:] == "00300":
        output_name = "dissolved-oxygen-mgl"
    elif input_name[-8:] == "00300_cd":
        output_name = "dissolved-oxygen-mgl-qc"
    elif input_name[-5:] == "00301":
        output_name = "dissolved-oxygen-saturation-pct"
    elif input_name[-8:] == "00301_cd":
        output_name = "dissolved-oxygen-saturation-pct-qc"
    elif input_name[-5:] == "00400":
        output_name = "pH"
    elif input_name[-8:] == "00400_cd":
        output_name = "pH-qc"
    elif input_name[-5:] == "63680":
        output_name = "turbidity-fnu"
    elif input_name[-8:] == "63680_cd":
        output_name = "turbidity-fnu-qc"
    elif input_name[-5:] == "32295":
        output_name = "colored-dissolved-organic-matter-ppbqse"
    elif input_name[-8:] == "32295_cd":
        output_name = "colored-dissolved-organic-matter-ppbqse-qc"
    elif input_name[-5:] == "99133":
        output_name = "nitrate-as-n-mgl"
    elif input_name[-8:] == "99133_cd":
        output_name = "nitrate-as-n-mgl-qc"
    elif input_name[-5:] == "62361":
        output_name = "chlorophyll-ugl"
    elif input_name[-8:] == "62361_cd":
        output_name = "chlorophyll-ugl-qc"

    # FOX RIVER
    elif input_name == "NITROGEN, KJELDAHL, TOTAL, (MG/L AS N)":
        output_name = "nitrogen-kjeldahl-total-as-n-mgl"
    elif input_name == "NITRITE PLUS NITRATE, TOTAL 1 DET. (MG/L AS N)":
        output_name = "nitrate-nitrite-total-as-n-mgl"
    elif input_name == "PHOSPHORUS, TOTAL (MG/L AS P)":
        output_name = "phosphorus-total-as-p-mgl"
    elif input_name == "PHOSPHORUS, DISSOLVED (MG/L AS P)":
        output_name = "phosphorus-dissolved-as-p-mgl"
    elif input_name == "NITROGEN, AMMONIA, TOTAL (MG/L AS N)":
        output_name = "nitrogen-ammonia-total-as-n-mgl"
    elif input_name == "NITRATE NITROGEN, TOTAL (MG/L AS N)":
        output_name = "nitrate-nitrogen-total-as-n-mgl"
    elif input_name == "NITRITE NITROGEN, TOTAL (MG/L AS N)":
        output_name = "nitrite-nitrogen-total-as-n-mgl"
    elif input_name == "NITROGEN, ORGANIC, TOTAL (MG/L AS N)":
        output_name = "nitrogen-organic-total-as-n-mgl"
    elif input_name == "AMMONIA, UNIONZED                      (MG/L AS N)":
        output_name = "ammonia-unionized-as-n-mgl"
    elif input_name == "NITROGEN, TOTAL (MG/L AS N)":
        output_name = "nitrogen-total-as-n-mgl"
    elif input_name == "NITROGEN, TOTAL, AS NO3 - MG/L":
        output_name = "nitrogen-total-as-no3-mgl"
    elif input_name == "AMMONIA, UNIONIZED (CALC FR TEMP-PH-NH4)  (MG/L)":
        output_name = "ammonia-unionized-temp-ph-nh4-mgl"
    elif input_name == "PHOSPHATE, POLY (MG/L AS PO4)":
        output_name = "phosphate-poly-as-po4-mgl"
    elif input_name == "PHOSPHORUS,SED,BOT,<63,WET SIEVE,FIELD,TOTAL    %":
        output_name = "phosphorus-sed-bot-<63-wet-sieve-field-total-pct"
    elif input_name == "NITRITE PLUS NITRATE, DISS. 1 DET. (MG/L AS N)":
        output_name = "nitrite-plus-nitrate-diss-1det-as-n-mgl"
    elif input_name == "NITROGEN, AMMONIA, DISSOLVED (MG/L AS N)":
        output_name = "nitrogen-ammonia-dissolved-as-n-mgl"
    elif input_name == "NITRATE NITROGEN, DISSOLVED (MG/L AS NO3)":
        output_name = "nitrate-nitrogen-dissolved-as-no3-mgl"
    elif input_name == "NITROGEN, AMMONIA, DISSOLVED (MG/L AS NH4)":
        output_name = "nitrogen-ammonia-dissolved-as-nh4-mgl"
    elif input_name == "PHOSPHORUS,IN TOTAL ORTHOPHOSPHATE (MG/L AS P)":
        output_name = "phosphorus-in-total-orthophosphate-as-p-mgl"
    elif input_name == "PHOSPHORUS, DISSOLVED ORTHOPHOSPHATE (MG/L AS P)":
        output_name = "phosphorus-dissolved-orthophosphate-as-p-mgl"
    elif input_name == "PHOSPHATE, ORTHO (MG/L AS PO4)":
        output_name = "phosphate-ortho-as-po4-mgl"
    elif input_name == "NITRATE NITROGEN, DISSOLVED (MG/L AS N)":
        output_name = "nitrate-nitrogen-dissolved-as-n-mgl"
    elif input_name == "NITRITE NITROGEN, DISSOLVED (MG/L AS N)":
        output_name = "nitrite-nitrogen-dissolved-as-n-mgl"
    elif input_name == "NITRITE NITROGEN, DISSOLVED (MG/L AS NO2)":
        output_name = "nitrite-nitrogen-dissolved-as-no2-mgl"
    elif input_name == "NITROGEN, AMMONIA, TOTAL (MG/L AS NH4)":
        output_name = "nitrogen-ammonia-total-as-nh4-mgl"
    elif input_name == "PHOSPHATE, TOTAL (MG/L AS PO4)":
        output_name = "phosphate-total-as-po4-mgl"
    elif input_name == "AMMONIA -STATE OF ILLINOIS (MG/L)":
        output_name = "ammonia-mgl"
    elif input_name == "NITROGEN KJELDAHL TOTAL BOTTOM DEP DRY WT MG/KG":
        output_name = "nitrogen-kjeldahl-total-bottom-dep-dry-wt-Mgkg"
    elif input_name == "PHOSPHORUS,TOTAL,BOTTOM DEPOSIT (MG/KG-P DRY WGT)":
        output_name = "phosphorus-total-bottom-deposit-dry-wgt-Mgkg"
    elif input_name == "NITROGEN, KJELDAHL, DISSOLVED (MG/L AS N)":
        output_name = "nitrogen-kjeldahl-dissolved-as-n-mgl"
    elif input_name == "PHOSPHOROUS, SEDIMENT, SUSPENDED,          PERCENT":
        output_name = "phosphorus-sediment-suspended-pct"
    elif input_name == "NITROGEN, DISSOLVED (MG/L AS N)":
        output_name = "nitrogen-dissolved-as-n-mgl"
    elif input_name == "PHOSPHATE, TOTAL SOLUBLE (MG/L)":
        output_name = "phosphate-total-soluble-mgl"
    elif input_name == "NITROGEN, AMMONIA, BOTTOM DEPOSITS (MG/KG-N)":
        output_name = "nitrogen-ammonia-bottom-deposits-MgKg"
    elif input_name == "ORTHO-PHOSPHATE NES ALGAL ASSAY  MG/L":
        output_name = "ortho-phosphate-nes-algal-assay-mgl"
    elif input_name == "PHOSPHORUS,SED,BOT,<63,DRY SIEVE,LAB,TOTAL      %":
        output_name = "phosphorus-sed-bot-<63-dry-sieve-lab-totals-pct"

    # TENNESSEE
    elif input_name == "STATION ID":
        output_name = "sensor_name"
    elif input_name == "Activity Start Date":
        output_name = "start_date"
    elif input_name == "LATITUDE":
        output_name = "lat"
    elif input_name == "LONGITUDE":
        output_name = "long"
    elif input_name == "DO Clean NO":
        output_name = "dissolved-oxygen-mgl"
    elif input_name == "pH Clean NO":
        output_name = "ph"
    elif input_name == "Temp Clean NO":
        output_name = "temperature-c"
    elif input_name == "COND Clean NO":
        output_name = "conductivity-umhocm"
    elif input_name == "NO2_3 Clean NO":
        output_name = "nitrate-nitrite-as-n-mgl"
    elif input_name == "TP Clean NO":
        output_name = "total-phosphorus-mgl"
    elif input_name == "ORTHO P Clean NO":
        output_name = "phosphorus-dissolved-orthophosphate-as-p-mgl"
    elif input_name == "TKN Clean NO":
        output_name = "nitrogen-kjeldahl-total-as-n-mgl"
    elif input_name == "TOC Clean NO":
        output_name = "total-organic-carbon-mgl"
    elif input_name == "NH3 Clean NO":
        output_name = "ammonia-mgl"
    elif input_name == "TURB Clean NO":
        output_name = "turbidity-ntu"
    elif input_name == "E Coli Clean NO":
        output_name = "e-coli-mpndl"
    elif input_name == "Fecal Clean NO":
        output_name = "fecal-coliforms-mpndl"

    # ILLINOIS EPA
    elif input_name == "Station ID":
        output_name = "sensor_name"
    elif input_name == "Activity Start":
        output_name = "start_date"
    elif input_name == "Station Latitude":
        output_name = "lat"
    elif input_name == "Station Longitude":
        output_name = "long"
    elif input_name == "Activity Start Zone":
        output_name = "time_zone"

    # NOAA
    elif input_name == "sea_water_temperature":
        output_name = "water-temperature-c"

    # IWQIS
    elif input_name == "nitrate_con-iwqis":
        output_name = "nitrate-nitrite-as-n-mgl"
    elif input_name == "discharge-iwqis":
        output_name = "discharge-ft3s"
    elif input_name == "diss_oxy_con-iwqis":
        output_name = "dissolved-oxygen-mgl"
    elif input_name == "turbi_mean-iwqis":
        output_name = "water-turbidity-ntu"
    elif input_name == "temp_water-iwqis":
        output_name = "water-temperature-c"
    elif input_name == "ph-iwqis":
        output_name = "pH"
    elif input_name == "spec_cond-iwqis":
        output_name = "specific-conductivity-uscm"

    else:
        output_name = input_name

    return output_name
