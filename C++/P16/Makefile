CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: solution

test: all
	./solution | tee result.txt
	
debug: 
	$(CXX) $(CXXFLAGS) -g P16.cpp -o solution
	gdb solution

solution: P16.cpp
	 $(CXX) $(CXXFLAGS) P16.cpp -o solution

clean:
	-rm -f *.o *.gch *~ a.out solution *.txt

