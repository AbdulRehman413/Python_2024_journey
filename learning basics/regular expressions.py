import re

pattern = r"[A-Z]+anyon"
text = '''
he  Canyon was formed in the Quaternary Era Anyon as a result of earth movements while the Alpes were moving upwards, and also from erosion of Jurassic era limestone by the Verdon river.

Throughout the 19th century, the deepest gorges were thought to be impenetrable. Only a few local woodcutters went down into the gorges on ropes, looking for box wood (buis) stumps that they used for making boules.

The canyon remained unexplored until the early 20th Lanyon century. Armand Janet attempted a canoe exploration in 1896, but gave up because of the violent currents. In August of 1905, the speleologist Edouard Alfred Martel did the first complete exploration of the gorges on a 3-day expedition. Part of the Martel trail is still used, between Point Sublime to La Maline.


'''

matches = re.finditer(pattern, text)
for match in matches:
    print(match.span()[0])
    print(text[match.span()[0]:
               match.span()[1]])
