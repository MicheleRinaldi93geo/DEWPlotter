"""MAIN"""

# -------------------------------------------------------------------------------------------------
# LIBRARIES
import os
import pandas as pd
from DEWPlotter_lib import _functions as fnt
from termcolor import colored
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
"""MAIN"""
def analise(directory):
    # Setting working directory
    os.chdir(directory)

    # Getting the directory
    dirname = './Data & Plots/'

    fnt.check_files_in_folder()

    if not os.path.exists(dirname):
        os.makedirs(dirname)

    # Read in the tab file
    ph_tab = fnt.read_ph()
    solid_tab = fnt.read_solids()
    logmol_tab = fnt.read_logmoles()
    log_elements_tab = fnt.read_log_elements()
    dest_mol_tab = fnt.read_dest_mol()[0]
    dest_other_tab = fnt.read_dest_other()

    # Convert tab file information into Excel file
    writer = pd.ExcelWriter('%sData Tables.xlsx' % dirname)
    ph_tab.to_excel(writer, sheet_name='pH, T, log fo2')

    if solid_tab is not None: solid_tab.to_excel(writer, sheet_name='Solid Solutions')
    if logmol_tab is not None: logmol_tab.to_excel(writer, sheet_name='log(moles) Minerals')

    log_elements_tab.to_excel(writer, sheet_name='log(moles) Dissolved Elements')
    dest_mol_tab.to_excel(writer, sheet_name='log(moles) Destroyed')
    dest_other_tab.to_excel(writer, sheet_name='Created & Destroyed (g & cc)')

    # Useful only when carbon is included
    log_conc_tab = fnt.read_log_conc()
    log_conc_tab.to_excel(writer, sheet_name='Log Concentrations')

    # New total moles of fluid species tab doesn't work yet
    moles_dissolved_tab = fnt.read_moles_dissolved()
    # moles_dissolved_tab.to_excel(writer, 'Moles fluid species')

    # New oxide concentrations tab
    oxide_conc_tab = fnt.read_oxide_conc()
    oxide_conc_tab.to_excel(writer, sheet_name='Oxide Conc')

    writer.close()

    fnt.tab_plot(dirname, logmol_tab.iloc[1:, 2:], 'log(moles) Minerals', logmol_tab.columns[2:]) if (
            logmol_tab is not None) else print("No mineral product data.")
    fnt.tab_plot(dirname, solid_tab.iloc[1:, :], "Solid Solution Compositions", solid_tab.columns) if (
            solid_tab is not None) else print("Solid solution disabled.")
    fnt.tab_plot(dirname, log_elements_tab.iloc[1:, :], "log(moles) Dissolved Elements", log_elements_tab.columns) if (
            log_elements_tab is not None) else print("No dissolved element data.")

    fnt.tab_plot(dirname, ph_tab.iloc[1:, 0], "Temperature °C", ['Temperature °C'])
    fnt.tab_plot(dirname, ph_tab.iloc[1:, 1], "pH", ['pH'])
    fnt.tab_plot(dirname, ph_tab.iloc[1:, 2], "log fO2", ['log fO2'])

    # Useful only when carbon is included
    fnt.tab_plot(dirname, log_conc_tab.iloc[1:, :], "log Concentrations", log_conc_tab.columns)

    print(colored('Analysis completed', 'green'))
    print('')
# -------------------------------------------------------------------------------------------------
