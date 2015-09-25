s := s0; e := E(s)                  // Initial state, energy.
sb := s; eb := e                    // Initial "best" solution
k := 0                              // Energy evaluation count.
WHILE k < kmax and e > emax         // While time remains & not good enough:
  sn := neighbor(s)                 //   Pick some neighbor.
  en := E(sn)                       //   Compute its energy.
  IF    en < eb                     //   Is this a new best?
  THEN  sb := sn; eb := en          //     Yes, save it.
        print "!"
  FI
  IF    en < e                      // Should we jump to better?
  THEN  s := sn; e := en            //    Yes!
        print "+"                        
  FI
  ELSE IF P(e, en, k/kmax) < rand() // Should we jump to worse?
  THEN  s := sn; e := en            //    Yes, change state.
        print "?"
  FI
  print "."
  k := k + 1                        //   One more evaluation done    
  if k % 50 == 0: print "\n",sb
RETURN sb                           // Return the best solution found.