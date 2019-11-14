CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: solution

test: all
	./solution | tee result.txt
	
debug: 
	$(CXX) $(CXXFLAGS) -g P15.cpp -o solution
	gdb solution

solution: P15.cpp
	 $(CXX) $(CXXFLAGS) P15.cpp -o solution

clean:
	-rm -f *.o *.gch *~ a.out solution *.txt

