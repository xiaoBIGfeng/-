=COUNTIF(D2:D883, "<=-0.1")
=COUNTIF(G2:G883, "<=-0.1")
=COUNTIF(J2:J883, "<=-0.1")
=COUNTIFS(D2:D883, "<=-0.1", G2:G883, "<=-0.1", J2:J883, "<=-0.1")
=TEXTJOIN(",", TRUE, IF((D2:D883<=-0.1)*(G2:G883<=-0.1)*(J2:J883<=-0.1), A2:A883, ""))

=SUMPRODUCT((D2:D883<0) * (G2:G883<0) * (J2:J883<0) * ((D2:D883<=-0.1) + (G2:G883<=-0.1) + (J2:J883<=-0.1) > 0))
=TEXTJOIN(",", TRUE, IF((D2:D883<0) * (G2:G883<0) * (J2:J883<0) * ((D2:D883<=-0.1) + (G2:G883<=-0.1) + (J2:J883<=-0.1) > 0), A2:A883, ""))
=TEXTJOIN(",", TRUE, IF((D2:D883<0) * (G2:G883<0) * (J2:J883<0) * (MIN(D2:D883, G2:G883, J2:J883)<=-0.1), A2:A883, ""))

31+11+17+13+17+14+10+8+13+11+13+13+13=184
184/882=0.2086

