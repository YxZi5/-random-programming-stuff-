Funkcja dec_bin() konwertuje decymalną liczbe zmiennoprzecinkową (float) na wartość w systemie binarnym - zwraca liczbe binarna jako string. Funkcja bin_dec konwertuje liczbe zmiennoprzecinkową zapisaną w systemie binarnym na wartość decymalną. Obie funkjce posiadają drugi parametr który wskazuje na ilość bitów danej liczby tzn: istnieją liczby typu float np: 0.2 które decymalnie można zapisać tylko jako wartość w przybliżeniu chyba że zapisujemy liczbe 0.2 na 64 bitach przykład ten jednak działa tylko dla liczby "0.2". Dlatego też funkcje posiadają taki parametr w którym określić można jaką długość bitową ma posiadać dana liczba - co ma swój skutek w momencie kiedy liczbe float w systemie binarnym konwertujemy na liczbe dziesiętną.