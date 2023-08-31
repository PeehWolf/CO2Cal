import geopandas as gpd

#Leitura dos dados de micro e meso regiao, tambem separacao dos municipios 

def carregar_geodados():
    GDMunicipio = gpd.read_file('Geodata/MS_Municipios_2022.shp')
    GDMesoregiao = gpd.read_file('Geodata/MS_Mesorregioes_2022.shp')
    GDMicrorregiao = gpd.read_file('Geodata/MS_Microrregioes_2022.shp')
    GDAnalise = gpd.read_file('Geodata/Area_de_Analise/FAZ_STO_ANTONIO_PABLO.geojson')
    return GDMunicipio, GDMesoregiao, GDMicrorregiao, GDAnalise

