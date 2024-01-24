class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"
    
    def evaluate(self, x_val):
        return x_val

class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)
    
    def evaluate(self, x_val):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)
    
    def evaluate(self, x_val):
        return self.p1.evaluate(x_val) + self.p2.evaluate(x_val)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)
    
    def evaluate(self, x_val):
        return self.p1.evaluate(x_val) * self.p2.evaluate(x_val)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1  
        self.p2 = p2  

    def __repr__(self):
        if isinstance(self.p2, (Add, Sub)):
            return repr(self.p1) + " - (" + repr(self.p2) + ")"
        return repr(self.p1) + " - " + repr(self.p2)
    
    def evaluate(self, x_val):
        return self.p1.evaluate(x_val) - self.p2.evaluate(x_val)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1  
        self.p2 = p2  

    def __repr__(self):
        numerator = repr(self.p1)
        denominator = repr(self.p2)
        
        if isinstance(self.p1, (Add, Sub)):
            numerator = "( " + numerator + " )"
        if isinstance(self.p2, (Add, Sub)):
            denominator = "( " + denominator + " )"
        
        return numerator + " / " + denominator
    
    def evaluate(self, x_val):
        denominator = self.p2.evaluate(x_val)
        if denominator == 0:
            raise ValueError("Division by zero is undefined")
        return self.p1.evaluate(x_val) / denominator

poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)

# Example usage:
p1 = Add(X(), Int(2)) 
p2 = Mul(X(), Int(3))  

sub_expr = Sub(p1, p2)  
div_expr = Div(p1, p2)  

print(sub_expr)  
print(div_expr) 

poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly.evaluate(-1))
