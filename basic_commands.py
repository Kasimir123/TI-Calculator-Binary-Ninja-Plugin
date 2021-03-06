basic_commands = {
    #Base TI84 language

    b'': "&null", # Use &null to tell the compiler to break up the next statement
    b'\x01': ">DMS", # Angle>DMS        (Displays Angle in degrees/minutes/seconds format)
    b'\x02': ">DEC", # Value>DEC (Displays Value in decimal format)
    b'\x03': ">FRAC", # Value>FRAC (Displays Value as a Fraction in simplest terms)
    b'\x04': "->", # Value->Variable (Assigns Value to Variable)
    b'\x05': "Boxplot",
    b'\x06': "[",
    b'\x07': "]",
    b'\x08': "{",
    b'\t': "}",
    b'\n': "&rad", # Angle&rad (Interprets Angle in radians)
    b'\x0b': "&deg", # Angle&deg (Interprets Angle in degrees)
    b'\x0c': "&^-1", # Value^-1 (Returns the inverse of Value)
    b'\r': "&^2", # Value^2 (Returns Value squared)
    b'\x0e': "&transpose", # Matrix&transpose (Transpose: Returns (row,column)¸(column,row))
    b'\x0f': "&^3", # Value^3 (Returns Value cubed)
    b'\x10': "(",
    b'\x11': ")",
    b'\x12': "round(", # round(Value[,#Decimals]) (Returns Value rounded to #Decimals. Default=0)
    b'\x13': "pxl-Test(", # pxl-Test(Row,Column) (Returns 1 if pixel is On, 0 if pixel is Off)
    b'\x14': "augment(", # augment(ListA,ListB) (Returns ListB Concatenated to the end of ListA)
    b'\x15': "rowSwap(", # rowSwap(Matrix,RowA,RowB) (Returns RowA swapped with RowB)
    b'\x16': "row+(", # row+(Matrix,RowA,RowB) (Returns RowA added to RowB, stored in RowB
    b'\x17': "*row(", # *row(Value,Matrix,Row) (Returns Row multiplied by Value, stored in Row)
    b'\x18': "*row+(", # *row+(Value,Matrix,RowA,RowB) (Returns RowA*Value+RowB, stored in RowB)
    b'\x19': "max(", # max(ValueA,ValueB) max(List) max(ListA,ListB) max(Value,List) (Rtn high val of each pair)
    b'\x1a': "min(", # min(ValueA,ValueB) min(List) min(ListA,ListB) min(Value,List) (Rtn low val of each pair)
    b'\x1f': "median(", # median(List[,Freqlist]) (Returns median of List with frequency Freqlist)
    b' ': "randM(", # randM(Rows,Columns) (Returns a random matrix of the dimension (Rows * Columns))
    b'!': "mean(", # mean(List[,Freqlist]) (Returns mean of List with frequency Freqlist)
    b'"': "solve(", # solve(Expression,Variable,Guess,{Lower,Upper}) (Solves Expression for Variable)
    b'#': "seq(", # seq(Expression,Variable,Begin,End[,Increment]) (Returns list of solutions)
    b'$': "fnInt(", # fnInt(Expression,Variable,Lower,Upper[,Tolerance]) (Returns integral of Expression)
    b'%': "nDeriv(", # nDeriv(Expression,Variable,Value[,h]) (Returns approx num deriv of Expr w/ Variable at Value)
    b"'": "fMin(", # fMin(Expression,Variable,Lower,Upper[,Tolerance]) (Returns minimum value of Expression)
    b'(': "fMax(", # fMax(Expression,Variable,Lower,Upper[,Tolerance]) (Returns maximum value of Expression)
    b')': " ",
    b'*': "\"", # "Textstring" (Returns a string containing Textstring)
    b'+': ",",
    b',': "&i", # i (imaginary i=(-1)^(1/2))
    b'-': "!", # Value! (factorial (Value!)=(Value-1)!*Value)
    b'0': "0",
    b'1': "1",
    b'2': "2",
    b'3': "3",
    b'4': "4",
    b'5': "5",
    b'6': "6",
    b'7': "7",
    b'8': "8",
    b'9': "9",
    b':': ".",
    b';': "&E", # Value&EPower (Used in scientific notation. Same as Value*10^Power)
    b'<': " or ", # ValueA or ValueB (Logical OR operator)
    b'=': " xor ", # ValueA or ValueB (Logical XOR operator, same as (A OR B) AND NOT (A AND B))
    b'>': ":", # Denotes a new line of code
    b'?': "\r\n",
    b'@': " and ", # ValueA and ValueB (Logical AND operator)
    b'A': "A",
    b'B': "B",
    b'C': "C",
    b'D': "D",
    b'E': "E",
    b'F': "F",
    b'G': "G",
    b'H': "H",
    b'I': "I",
    b'J': "J",
    b'K': "K",
    b'L': "L",
    b'M': "M",
    b'N': "N",
    b'O': "O",
    b'P': "P",
    b'Q': "Q",
    b'R': "R",
    b'S': "S",
    b'T': "T",
    b'U': "U",
    b'V': "V",
    b'W': "W",
    b'X': "X",
    b'Y': "Y",
    b'Z': "Z",
    b'[': "&theta", # The Greek letter Theta
    b'\\\x00': "[A]",
    b'\\\x01': "[B]",
    b'\\\x02': "[C]",
    b'\\\x03': "[D]",
    b'\\\x04': "[E]",
    b'\\\x05': "[F]",
    b'\\\x06': "[G]",
    b'\\\x07': "[H]",
    b'\\\x08': "[I]",
    b'\\\t': "[J]",
    b']\x00': "&L1",
    b']\x01': "&L2",
    b']\x02': "&L3",
    b']\x03': "&L4",
    b']\x04': "&L5",
    b']\x05': "&L6",
    b'^\x10': "&Y1",
    b'^\x11': "&Y2",
    b'^\x12': "&Y3",
    b'^\x13': "&Y4",
    b'^\x14': "&Y5",
    b'^\x15': "&Y6",
    b'^\x16': "&Y7",
    b'^\x17': "&Y8",
    b'^\x18': "&Y9",
    b'^\x19': "&Y0",
    b'^ ': "&X1T",
    b'^!': "&Y1T",
    b'^"': "&X2T",
    b'^#': "&Y2T",
    b'^$': "&X3T",
    b'^%': "&Y3T",
    b'^&': "&X4T",
    b"^'": "&Y4T",
    b'^(': "&X5T",
    b'^)': "&Y5T",
    b'^*': "&X6T",
    b'^+': "&Y6T",
    b'^@': "&r1",
    b'^A': "&r2",
    b'^B': "&r3",
    b'^C': "&r4",
    b'^D': "&r5",
    b'^E': "&r6",
    b'^\x80': "&u",
    b'^\x81': "&v",
    b'^\x82': "&w",
    b'_': "prgm",
    b'`\x00': "Pic1",
    b'`\x01': "Pic2",
    b'`\x02': "Pic3",
    b'`\x03': "Pic4",
    b'`\x04': "Pic5",
    b'`\x05': "Pic6",
    b'`\x06': "Pic7",
    b'`\x07': "Pic8",
    b'`\x08': "Pic9",
    b'`\t': "Pic0",
    b'a\x00': "GDB1",
    b'a\x01': "GDB2",
    b'a\x02': "GDB3",
    b'a\x03': "GDB4",
    b'a\x04': "GDB5",
    b'a\x05': "GDB6",
    b'a\x06': "GDB7",
    b'a\x07': "GDB8",
    b'a\x08': "GDB9",
    b'a\t': "GDB0",
    b'b!': "&eta", # The Greek letter eta
    b'd': "Radian", # Set Radian mode
    b'e': "Degree", # Set Degree mode
    b'f': "Normal", # Normal notation
    b'g': "Sci", # Scientific notation
    b'h': "Eng", # Engineering notation
    b'i': "Float", # Floating Point notation
    b'j': "=", # Test for equality
    b'k': "<", # Is less than
    b'l': ">", # Is greater than
    b'm': "<=", # Is less than or equal to
    b'n': ">=", # Is greater than or equal to
    b'o': "!=", # Is not equal to
    b'p': "+",
    b'q': "-",
    b'r': "Ans", # (Returns the previous answer)
    b's': "Fix", # Fix # (Sets fixed decimal notation to # places)
    b't': "Horiz", # Horiz (Horizontal split-screen mode)
    b'u': "Full", # Full (Sets Fullscreen mode)
    b'v': "Func", # Func (Sets Function graphing mode)
    b'w': "Param", # Param (Sets Parametric graphing mode)
    b'x': "Polar", # Polar (Sets Polar graphing mode)
    b'y': "Seq", # Seq (Sets Sequence graphing mode)
    b'z': "IndpntAuto",
    b'{': "IndpntAsk",
    b'|': "DependAuto",
    b'}': "DependAsk",
    b'~\x00': "Sequential", # Sequential (Draw graphs one at a time)
    b'~\x01': "Simul", # Simul (Draw graphs simultaneously)
    b'~\x02': "PolarGC",
    b'~\x03': "RectGC",
    b'~\x04': "CoordOn",
    b'~\x05': "CoordOff",
    b'~\x06': "Connected", # (Connect points on graph)
    b'~\x07': "Dot", # (Don't connect points on graph)
    b'~\x08': "AxesOn", # (Display axes on graph)
    b'~\t': "AxesOff", # (Don't display axes on graph)
    b'~\n': "GridOn", # (Display the grid)
    b'~\x0b': "GridOff", # (Don't display the grid)
    b'~\x0c': "LabelOn", # (Label the graphs)
    b'~\r': "LabelOff", # (Don't label the graphs)
    b'~\x0e': "Web", # (Draw seuence graphs as webs)
    b'~\x0f': "Time", # (Draw sequence graphs over time)
    b'~\x10': "uvAxes",
    b'~\x11': "uwAxes",
    b'~\x12': "vwAxes",
    b'\x7f': "&square", # Square mark
    b'\x80': "&plus", # Plus mark
    b'\x81': "&dot", # Dot mark
    b'\x82': "*",
    b'\x83': "/",
    b'\x84': "Trace",
    b'\x85': "ClrDraw", # (Clear the graph window)
    b'\x86': "ZStandard", # (Standard zoom)
    b'\x87': "ZTrig", # (Trig zoom)
    b'\x88': "ZBox",
    b'\x89': "Zoom In",
    b'\x8a': "Zoom Out",
    b'\x8b': "ZSquare", # (Zoom to give each pixel has an equal height and width)
    b'\x8c': "ZInteger", # (Zoom to give each pixel a height and width of 1)
    b'\x8d': "ZPrevious",
    b'\x8e': "ZDecimal", # (Zoom to give each pixel a height and width of 0.1)
    b'\x8f': "ZoomStat",
    b'\x90': "ZoomRcl",
    b'\x92': "ZoomSto",
    b'\x93': "Text(", # Text(Row,Column,Text1[,Text2,..,Textn]) (Draws text on the graph)
    b'\x94': " nPr ",
    b'\x95': " nCr ",
    b'\x96': "FnOn ", # FnOn [Function#,Function#...] (Enables all [specified] functions)
    b'\x97': "FnOff ", # FnOff [Function#,Function#...] (Disables all [specified] functions)
    b'\x98': "StorePic ", # StorePic # (Stores a screenshot in Pic#)
    b'\x99': "RecallPic ", # RecallPic # (Displays the screenshot stored in Pic#)
    b'\x9a': "StoreGDB ",
    b'\x9b': "RecallGDB ",
    b'\x9c': "Line(", # Line(X1,Y1,X2,Y2[,0]) (Draws a line from (X1,Y1) to (X2,Y2) on the graph. Add 0 to erase.)
    b'\x9d': "Vertical ", # Vertical x (Draws a vertical line at x)
    b'\x9e': "Pt-On(", # Pt-On(x,y[,mark]) (Draws a point at (x,y) with mark)
    b'\x9f': "Pt-Off(", # Pt-Off(x,y[,mark]) (Erases a point at (x,y) with mark)
    b'\xa0': "Pt-Change(", # Pt-Change(x,y) (Toggles the point at (x,y))
    b'\xa1': "Pxl-On(", # Pxl-On(Row,Column) (Draws the pixel at (Row,Column))
    b'\xa2': "Pxl-Off(", # Pxl-Off(Row,Column) (Erases the pixel at (Row,Column))
    b'\xa3': "Pxl-Change(", # Pxl-Change(Row,Column) (Toggles the pixel at (Row,Column))
    b'\xa4': "Shade(", # Shade(Lowerfunc,Upperfunc[,Xleft,Xright,Pattern,Patres]) (See manual for details)
    b'\xa5': "Circle(", # Circle(x,y,r) (Draws a circle with center (x,y) and radius r)
    b'\xa6': "Horizontal ", # Horizontal y (Draws a horizontal line at y)
    b'\xa7': "Tangent(", # Tangent(Expression,Value) (Draws a line tangent to Expression at Value)
    b'\xa8': "DrawInv ", # DrawInv Expression (Plots the inverse of Expression by plotting X values on the Y axis)
    b'\xa9': "DrawF ", # DrawF Expression (Plots Expression)
    b'\xaa\x00': "Str1",
    b'\xaa\x01': "Str2",
    b'\xaa\x02': "Str3",
    b'\xaa\x03': "Str4",
    b'\xaa\x04': "Str5",
    b'\xaa\x05': "Str6",
    b'\xaa\x06': "Str7",
    b'\xaa\x07': "Str8",
    b'\xaa\x08': "Str9",
    b'\xaa\t': "Str0",
    b'\xab': "rand", # rand[(Numtrials)] (Returns a random number from 0 to 1)
    b'\xac': "&pi", # The Greek letter pi is approximated at 3.1415926545898
    b'\xad': "getKey", # getKey (Returns the last key pressed or 0 for no key. See Tools>Button List for details.)
    b'\xae': "'",
    b'\xaf': "?",
    b'\xb0': "&-", # The negative sign. This is a different key from subtraction!
    b'\xb1': "int(", # int(Value) (Returns the largest integer ˜ Value)
    b'\xb2': "abs(", # abs(Value) (Returns the absolute value of Value)
    b'\xb3': "det(", # det(Matrix) (Returns the Determinant of Matrix)
    b'\xb4': "identity(", # identity(Dimension) (Returns the identity matrix of Dimension rows and columns)
    b'\xb5': "dim(", # Length->dim(List) {Rows,Columns}->dim(Matrix) (Gives List/Matrix the specified dimension(s))
    b'\xb6': "sum(", # sum(List[,Start,End]) (Returns the sum of values in List from Start to End)
    b'\xb7': "prod(", # prod(List[,Start,End]) (Returns the product of values in List from Start to End)
    b'\xb8': "not(", # not(Value) (If Value>0, returns 0. If Value=0, returns 1)
    b'\xb9': "iPart(", # iPart(Value) (Returns the integer part of a number)
    b'\xba': "fPart(", # fPart(Value) (Returns the fraction part of a number)
    b'\xbb\x07': "dbd(", # dbd(DDMM.YY, DDMM.YY) (Returns the number of days between two dates)
    b'\xbb\x08': "lcm(", # lcm(ValueA,ValueB) (Returns the least common multiple of ValueA and ValueB)
    b'\xbb\t': "gcd(", # gcd(ValueA,ValueB) (Returns the greatest common factor of ValueA and ValueB)
    b'\xbb\n': "randInt(", # randInt(Lower,Upper[,numtrials]) (Returns a random integer between Lower and Upper
    b'\xbb\x0b': "randBin(",
    b'\xbb\x0c': "sub(", # sub(String,Begin,Length) (Returns part of String starting at Begin of length Length)
    b'\xbb\r': "stdDev(", # stdDev(List[,Freqlist]) (Returns the standard derivation of the elements in List)
    b'\xbb\x0e': "variance(", # variance(List[,Freqlist]) (Returns the variance of the elements in List)
    b'\xbb\x0f': "inString(", # inString(String,Find[,Start]) (Returns position of the first instance of Find in String)
    b'\xbb%': "conj(", # conj(Value) (Returns the complex conjugate of Value)
    b'\xbb&': "real(", # real(Value) (Returns the real part of a complex number or numbers)
    b"\xbb'": "imag(", # imag(Value) (Returns the imaginary part of a complex number or numbers)
    b'\xbb(': "angle(", # angle(Value) (Returns the polar angle of a complex number or numbers)
    b'\xbb)': "cumSum(", # sumSum(List) (Returns a list of the cumulative sums of the elements in List)
    b'\xbb*': "expr(", # expr(String) (Converts String to an expression and executes it)
    b'\xbb+': "length(", # length(String) (Returns the number of characters in String)
    b'\xbb,': "&deltaList(", # &deltaList(List) (Returns the difference between consecutive terms in a list, as a list)
    b'\xbb-': "ref(", # ref(Matrix) (Returns the row-echelon form of Matrix)
    b'\xbb.': "rref(", # rref(Matrix) (Returns the reduced row-echelon form of Matrix)
    b'\xbb/': ">Rect",
    b'\xbb0': ">Polar",
    b'\xbb1': "&e", # Euler's constant is approximated at 2.718281828459
    b'\xbb9': "Matr>list(",
    b'\xbb:': "List>matr(",
    b'\xbbE': "GraphStyle(",
    b'\xbbM': "Real", # Real (Sets real number mode)
    b'\xbbN': "&re^thetai", # (Sets polar complex number mode)
    b'\xbbO': "&a+bi", # (Sets rectangular complex number mode)
    b'\xbbP': "ExprOn", # ExprOn (Turns on expression display during Trace)
    b'\xbbQ': "ExprOff", # ExprOff (Turns off expression display during Trace)
    b'\xbbR': "ClrAllLists", # ClrAllLists (Clears all lists from memory)
    b'\xbbS': "GetCalc(", # GetCalc(Variable[,Portflag]) (See the manual for details)
    b'\xbbT': "DelVar ", # DelVar Variable (Deletes Variable from memory)
    b'\xbbU': "Equ>String(", # Equ>String(Yvar,Str#) (Converts Yvar into a string and stores it in Str#)
    b'\xbbV': "String>Equ(", # String>Equ(String,Yvar) (Converts String to an expression and stores it in Yvar)
    b'\xbbW': "Clear Entries", # Clear Entries (Clears the Last Entry storage area)
    b'\xbbd': "&G-T", # G-T (Sets graph-table vertical split screen mode)
    b'\xbbe': "ZoomFit", # ZoomFit (Zooms the graph to include all minimums and maximums
    b'\xbbf': "DiagnosticOn",
    b'\xbbg': "DiagnosticOff",
    b'\xbbh': "Archive ", # Archive Variable (Stores Variable in flash memory)
    b'\xbbi': "UnArchive ", # UnArchive  Variable (Stores Variable in RAM memory)
    b'\xbbj': "Asm(", # Asm(Program) (Executes an assembly-language program)
    b'\xbbk': "AsmComp(", # AsmComp(Asciiprogram,Hexprogram) (Compiles an Ascii asm program, stores it in Hexprogram)
    b'\xbbl': "AsmPrgm", # AsmPrgm (Use this at the heading of an assembly-language program)
    b'\xbbm': "compiled asm",
    b'\xbbn': "Á",
    b'\xbbo': "À",
    b'\xbbp': "Â",
    b'\xbbq': "Ä",
    b'\xbbr': "á",
    b'\xbbs': "à",
    b'\xbbt': "â",
    b'\xbbu': "ä",
    b'\xbbv': "É",
    b'\xbbw': "È",
    b'\xbbx': "Ê",
    b'\xbby': "Ë",
    b'\xbbz': "é",
    b'\xbb{': "è",
    b'\xbb|': "ê",
    b'\xbb}': "ë",
    b'\xbb\x7f': "Ì",
    b'\xbb\x80': "Î",
    b'\xbb\x81': "Ï",
    b'\xbb\x82': "í",
    b'\xbb\x83': "ì",
    b'\xbb\x84': "î",
    b'\xbb\x85': "ï",
    b'\xbb\x86': "Ó",
    b'\xbb\x87': "Ò",
    b'\xbb\x88': "Ô",
    b'\xbb\x89': "Ö",
    b'\xbb\x8a': "ó",
    b'\xbb\x8b': "ò",
    b'\xbb\x8c': "ô",
    b'\xbb\x8d': "ö",
    b'\xbb\x8e': "Ú",
    b'\xbb\x8f': "Ù",
    b'\xbb\x90': "Û",
    b'\xbb\x91': "Ü",
    b'\xbb\x92': "ú",
    b'\xbb\x93': "ù",
    b'\xbb\x94': "û",
    b'\xbb\x95': "ü",
    b'\xbb\x96': "Ç",
    b'\xbb\x97': "ç",
    b'\xbb\x98': "Ñ",
    b'\xbb\x99': "ñ",
    b'\xbb\x9a': "´",
    b'\xbb\x9b': "`",
    b'\xbb\x9c': "&\"", # An extra doublequote for some reason
    b'\xbb\x9d': "&?", # The upside down question mark
    b'\xbb\x9e': "&!", # The upside down exclamation point
    b'\xbb\x9f': "&alpha", # The Greek letter Alpha
    b'\xbb\xa0': "&beta", # The Greek letter Beta
    b'\xbb\xa1': "&gamma", # The Greek letter Gamma
    b'\xbb\xa2': "&delta", # The Greek letter Delta
    b'\xbb\xa3': "&ldelta", # The Greek letter Delta (lowercase)
    b'\xbb\xa4': "&epsilon", # The Greek letter Epsilon
    b'\xbb\xa5': "&lambda", # The Greek letter Lambda
    b'\xbb\xa6': "&mu", # The Greek letter Mu
    b'\xbb\xa7': "&xpi", # For some reason, Pi has two characters
    b'\xbb\xa8': "&rho", # The Greek letter Rho
    b'\xbb\xa9': "&sigma", # The Greek letter Sigma
    b'\xbb\xab': "&phi", # The Greek letter Phi
    b'\xbb\xac': "&omega", # The Greek letter Omega
    b'\xbb\xae': "&chi", # The Greek letter Chi
    b'\xbb\xb0': "a",
    b'\xbb\xb1': "b",
    b'\xbb\xb2': "c",
    b'\xbb\xb3': "d",
    b'\xbb\xb4': "e",
    b'\xbb\xb5': "f",
    b'\xbb\xb6': "g",
    b'\xbb\xb7': "h",
    b'\xbb\xb8': "i",
    b'\xbb\xb9': "j",
    b'\xbb\xba': "k",
    b'\xbb\xbc': "l",
    b'\xbb\xbd': "m",
    b'\xbb\xbe': "n",
    b'\xbb\xbf': "o",
    b'\xbb\xc0': "p",
    b'\xbb\xc1': "q",
    b'\xbb\xc2': "r",
    b'\xbb\xc3': "s",
    b'\xbb\xc4': "t",
    b'\xbb\xc5': "u",
    b'\xbb\xc6': "v",
    b'\xbb\xc7': "w",
    b'\xbb\xc8': "x",
    b'\xbb\xc9': "y",
    b'\xbb\xca': "z",
    b'\xbb\xcb': "&lsigma", # The Greek letter Sigma (lowercase)
    b'\xbb\xcc': "&smallT1",
    b'\xbb\xcd': "Í",
    b'\xbb\xce': "GarbageCollect", # Defragment, clean up memory
    b'\xbb\xcf': "~",
    b'\xbb\xd1': "@",
    b'\xbb\xd2': "#",
    b'\xbb\xd3': "$",
    b'\xbb\xd4': "&&", # The ampersand must be escaped, as it is the escape character
    b'\xbb\xd5': "`",
    b'\xbb\xd6': ";",
    b'\xbb\xd7': "\\",
    b'\xbb\xd8': "|",
    b'\xbb\xd9': "_",
    b'\xbb\xda': "%", # Number% (Converts number to a percentage. NOT MODULUS OPERATOR)
    b'\xbb\xdb': "&...", # Elipsis
    b'\xbb\xdc': "&angle", # Angle symbol
    b'\xbb\xdd': "&beta", # The Greek letter Beta
    b'\xbb\xde': "&smallx1",
    b'\xbb\xdf': "&smallT2",
    b'\xbb\xe0': "&small0",
    b'\xbb\xe1': "&small1",
    b'\xbb\xe2': "&small2",
    b'\xbb\xe3': "&small3",
    b'\xbb\xe4': "&small4",
    b'\xbb\xe5': "&small5",
    b'\xbb\xe6': "&small6",
    b'\xbb\xe7': "&small7",
    b'\xbb\xe8': "&small8",
    b'\xbb\xe9': "&small9",
    b'\xbb\xea': "&small10",
    b'\xbb\xeb': "&leftarrow",
    b'\xbb\xec': "&rightarrow",
    b'\xbb\xed': "&uparrowsmall",
    b'\xbb\xee': "&downarrowsmall",
    b'\xbb\xef': "&smallx2",
    b'\xbb\xf0': "&integral", # The Integral symbol
    b'\xbb\xf1': "&uparrow",
    b'\xbb\xf2': "&downarrow",
    b'\xbb\xf3': "&squareroot",
    b'\xbb\xf4': "&highlightedequals", # A highlighted equals sign
    b'\xbc': "&squareroot(", # &squareroot(Value) (Returns the square root of Value)
    b'\xbd': "&cuberoot(", # &cuberoot(Value) (Returns the cube root of Value)
    b'\xbe': "ln(", # ln(Value) (Returns the natural logarithm of Value)
    b'\xbf': "&e^(", # e^(Value) (Returns e to the power of Value)
    b'\xc0': "log(", # log(Value) (Returns the logarithm of Value)
    b'\xc1': "10^(", # 10^(Value) (Returns 10 to the power of Value)
    b'\xc2': "sin(", # sin(Value) (Returns the sine of Value)
    b'\xc3': "&arcsin(", # &arcsin(Value) (Returns the arcsine of Value)
    b'\xc4': "cos(", # cos(Value) (Returns the cosine of Value)
    b'\xc5': "&arccos(", # &arccos(Value) (Returns the arccosine of Value)
    b'\xc6': "tan(", # tan(Value) (Returns the tangent of Value)
    b'\xc7': "&arctan(", # &arctan(Value) (Returns the arctangent of Value)
    b'\xc8': "sinh(", # sinh(Value) (Returns the hyperbolic sine of Value)
    b'\xc9': "&arcsinh(", # &arcsinh(Value) (Returns the hyperbolic arcsine of Value)
    b'\xca': "cosh(", # cosh(Value) (Returns the hyperbolic cosine of Value)
    b'\xcb': "&arccosh(", # &arccosh(Value) (Returns the hyperbolic arccosine of Value)
    b'\xcc': "tanh(", # tanh(Value) (Returns the hyperbolic tangent of Value)
    b'\xcd': "&arctanh(", # &arctanh(Value) (Returns the hyperbolic arctangent of Value)
    b'\xce': "If ", # If Condition:Command (If Condition=0, skips Command)
    b'\xcf': "Then", # If Condition:Then:Commands:Commands:End (If Condition=0, skips Commands)
    b'\xd0': "Else", # If Condition:Then:A:Else:B:End (If Condition=1, executes A. If Condition=0, executes B)
    b'\xd1': "While ", # While Condition:Commands:Commands:End (Executes Commands while Condition=True)
    b'\xd2': "Repeat ", # Repeat  Condition:Commands:Commands:End (Executes Commands until Condition=True)
    b'\xd3': "For(", # For(Variable,Begin,End[,Increment]):Commands:End (See manual for details)
    b'\xd4': "End", # End (See "For(", "If ", "Then", "Else", "While ", and "Repeat ")
    b'\xd5': "Return", # Return (Returns to the calling program)
    b'\xd6': "Lbl ", # Lbl Label (Creates a 1 or 2 letter label)
    b'\xd7': "Goto ", # Goto Label (Sends program execution to Label)
    b'\xd8': "Pause ", # Pause [Value] (Displays Value, suspends execution unitl the Enter key is pressed)
    b'\xd9': "Stop", # Stop (Ends program execution, returns to Home Screen)
    b'\xda': "IS>(", # IS>(Variable,Value):Command (Increments Variable by 1, skips Command if Variable>Value)
    b'\xdb': "DS<(", # DS<(Variable,Value):Command (Decrements Variable by 1, skips Command if Variable<Value)
    b'\xdc': "Input ", # Input ["Text",]Variable (Prompts for user to enter value, stores in Variable)
    b'\xdd': "Prompt ", # Prompt Variable[,Variable,Variable...] (Prompts user for variables in succession)
    b'\xde': "Disp ", # Disp Value[,Value,Value] (Displays each value as a new line on the home screen)
    b'\xdf': "DispGraph", # DispGraph (Displays the graph)
    b'\xe0': "Output(", # Output(Row,Column,Value) (Displays Value on the Home Screen starting at Row and Column)
    b'\xe1': "ClrHome", # ClrHome (Clears the Home Screen)
    b'\xe2': "Fill(", # Fill(Value,Matrix/List) (Fills Matrix/List with Value)
    b'\xe3': "SortA(", # SortA(List) (Sorts List elements in acending order)
    b'\xe4': "SortD(", # SortD(List) (Sorts List elements in decending order)
    b'\xe5': "DispTable", # DispTable (Displays the table)
    b'\xe6': "Menu(", # Menu("Title","Text1",Label1[,"Text2",Label2,...,"Text7",Label7]) (See Manual for details)
    b'\xe7': "Send(",
    b'\xe8': "Get(",
    b'\xeb': "&list", # &list (Identifies the next 1-5 characters as the name of a list)
    b'\xf0': "^",
    b'\xf1': "&root", # x&rooty (Returns y^(1/x))

    #Statistics tokens
    b'.': "CubicReg",
    b'/': "QuartReg",
    b'\x1b': "R>Pr(",
    b'\x1c': "R>Ptheta",
    b'\x1d': "P>Rx(",
    b'\x1e': "P>Ry",
    b'b\x01': "RegEq",
    b'b\x02': "n",
    b'b\x03': "xbar",
    b'b\x04': "sumx",
    b'b\x05': "sumx^2",
    b'b\x06': "Sx",
    b'b\x07': "sigmax",
    b'b\x08': "minX",
    b'b\t': "maxX",
    b'b\n': "minY",
    b'b\x0b': "maxY",
    b'b\x0c': "ybar",
    b'b\r': "sumy",
    b'b\x0e': "sumy^2",
    b'b\x0f': "Sy",
    b'b\x10': "sigmay",
    b'b\x11': "sumxy",
    b'b\x12': "r",
    b'b\x13': "Med",
    b'b\x14': "Q1",
    b'b\x15': "Q3",
    b'b\x16': "a",
    b'b\x17': "b",
    b'b\x18': "c",
    b'b\x19': "d",
    b'b\x1a': "e",
    b'b\x1b': "x1",
    b'b\x1c': "x2",
    b'b\x1d': "x3",
    b'b\x1e': "y1",
    b'b\x1f': "y2",
    b'b ': "y3",
    b'b!': "eta", # The Greek letter eta
    b'b"': "p", # p
    b'b#': "z", # z
    b'b$': "t", # t
    b'b%': "X^2", # X^2
    b'b&': "F", # F        (Statistics)
    b"b'": "df",
    b'b(': "pcarat",
    b'b)': "pcarat1",
    b'b*': "pcarat2",
    b'b+': "xbar1",
    b'b,': "Sx1",
    b'b-': "n1",
    b'b.': "xbar2",
    b'b/': "Sx2",
    b'b0': "n2",
    b'b1': "Sxp",
    b'b2': "lower",
    b'b3': "upper",
    b'b4': "s", # s
    b'b5': "r^2",
    b'b6': "R^2",
    b'b7': "Factordf",
    b'b8': "FactorSS",
    b'b9': "FactorMS",
    b'b:': "Errordf",
    b'b;': "ErrorSS",
    b'b<': "ErrorMS",
    b'\xbb\x10': "normalcdf(",
    b'\xbb\x11': "invNorm(",
    b'\xbb\x12': "tcdf(",
    b'\xbb\x13': "&X^2cdf(",
    b'\xbb\x14': "&Fcdf(",
    b'\xbb\x15': "binompdf(",
    b'\xbb\x16': "binomcdf(",
    b'\xbb\x17': "poissonpdf(",
    b'\xbb\x18': "poissoncdf(",
    b'\xbb\x19': "geometpdf(",
    b'\xbb\x1a': "geometcdf(",
    b'\xbb\x1b': "normalpdf(",
    b'\xbb\x1c': "tpdf(",
    b'\xbb\x1d': "&X^2pdf(",
    b'\xbb\x1e': "&Fpdf(",
    b'\xbb\x1f': "randNorm(",
    b'\xbb2': "SinReg ",
    b'\xbb3': "Logistic ",
    b'\xbb4': "LinRegTTest ",
    b'\xbb5': "ShadeNorm(",
    b'\xbb6': "Shade_t(",
    b'\xbb7': "ShadeX^2",
    b'\xbb8': "ShadeF(",
    b'\xbb9': "Matr>list(",
    b'\xbb:': "List>matr(",
    b'\xbb;': "Z-Test(",
    b'\xbb<': "T-Test ",
    b'\xbb=': "2-SampZTest(",
    b'\xbb>': "1-PropZTest(",
    b'\xbb?': "2-PropZTest(",
    b'\xbb@': "&X^2-Test(",
    b'\xbbA': "ZInterval ",
    b'\xbbB': "2-SampZInt(",
    b'\xbbC': "1-PropZInt(",
    b'\xbbD': "2-PropZInt(",
    b'\xbbF': "2-SampTTest ",
    b'\xbbG': "2-SampFTest ",
    b'\xbbH': "TInterval ",
    b'\xbbI': "2-SampTInt ",
    b'\xbbJ': "SetUpEditor ",
    b'\xbbK': "Pmt_End",
    b'\xbbL': "Pmt_Bgn",
    b'\xbbX': "Select(",
    b'\xbbY': "ANOVA(",
    b'\xbbZ': "ModBoxplot",
    b'\xbb[': "NormProbPlot",
    b'\xbb\xad': "&^p",
    b'\xbb\xae': "&chi", # The Greek letter Chi
    b'\xbb\xaf': "&F",
    b'\xe9': "PlotsOn ",
    b'\xea': "PlotsOff ",
    b'\xec': "Plot1(",
    b'\xed': "Plot2(",
    b'\xee': "Plot3(",
    b'\xf2': "1-VarStats ",
    b'\xf3': "2-VarStats ",
    b'\xf4': "LinReg(a+bx) ",
    b'\xf5': "ExpReg ",
    b'\xf6': "LnReg ",
    b'\xf7': "PwrReg ",
    b'\xf8': "Med-Med ",
    b'\xf9': "QuadReg ",
    b'\xfa': "ClrList ",
    b'\xfb': "ClrTable",
    b'\xfc': "Histogram",
    b'\xfd': "xyLine",
    b'\xfe': "Scatter",
    b'\xff': "LinReg(ax+b) ",

    #Financial tokens
    b'\xbb\x00': "npv(",
    b'\xbb\x01': "irr(",
    b'\xbb\x02': "bal(",
    b'\xbb\x03': "sumprn(",
    b'\xbb\x04': "sumInt(",
    b'\xbb\x05': ">Nom(",
    b'\xbb\x06': ">Eff(",
    b'\xbb ': "tmv_Pmt",
    b'\xbb!': "tmv_I%",
    b'\xbb"': "tmv_PV",
    b'\xbb#': "tmv_N",
    b'\xbb$': "tmv_FV",

    
    #Tokens used in the TI84+ and TI84s
    b'\xef\x00': "setDate(", # setDate(YYYY, MM, DD) (Sets the date)
    b'\xef\x01': "setTime(", # setTime(HH, MM, SS) (Sets the time in 24HR format)
    b'\xef\x02': "checkTmr(", # checkTmr(Variable) (Returns number of seconds since the timer stored in Variable)
    b'\xef\x03': "setDtFmt(", # setDtFmt(Format) (Set date display format: 1-M/D/Y 2-D/M/Y 3-Y/M/D)
    b'\xef\x04': "setTmFmt(", # setTmFmt(Format) (Set time display format: 12-12HR mode 24-24HR mode)
    b'\xef\x05': "timeCnv(", # timeCnv(Seconds) (Returns a list containing {D, H, M, S})
    b'\xef\x06': "dayOfWk(", # dayOfWk(YYYY, MM, DD) (Returns 1-7: 1=Sunday, 2=Monday, 3=Tuesday, etc...)
    b'\xef\x07': "getDtStr(", # getDtStr(Format) (Get a string representing the date. See setDtFmt for options.)
    b'\xef\x08': "getTmStr(", # getTmStr(Format) (Get a string representing the time. See setTmFmt for options.)
    b'\xef\t': "getDate", # getDate (Returns a list containing {Y, M, D})
    b'\xef\n': "getTime", # getTime (Returns a list containing {H, M, S})
    b'\xef\x0b': "startTmr", # startTmr->Variable (Start a new timer, store in Variable. See "checkTmr(")
    b'\xef\x0c': "getDtFmt", # getDtFmt (Return the current date display format: 1-M/D/Y 2-D/M/Y 3-Y/M/D)
    b'\xef\r': "getTmFmt", # getTmFmt (Return the current time display format: 12-12HR mode 24-24HR mode)
    b'\xef\x0e': "isClockOn", # isClockOn (Returns 1 if clock is on)
    b'\xef\x0f': "ClockOff", # ClockOff (Disables the clock in the Mode screen)
    b'\xef\x10': "ClockOn", # ClockOn (Enables the clock in the Mode screen)
    b'\xef\x11': "OpenLib(",
    b'\xef\x12': "ExecLib",
    b'\xef\x13': "invT(",
    b'\xef\x14': "X^2GOF-Test(",
    b'\xef\x15': "LinRegTInt",
    b'\xef\x16': "Manual-Fit"
}