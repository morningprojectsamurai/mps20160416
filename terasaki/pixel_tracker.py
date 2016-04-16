#this program is written by Python its version is 3.5.1
import numpy as np 

def generate_square_on_domain(domain_sizes=25):
    domain=np.zeros((domain_sizes,domain_sizes),dtype=int)
    #define test domain size
    row_size=14
    col_size=14
    upper_left_x=3
    upper_left_y=3
    #make square
    for i in range(row_size):
        domain[upper_left_x+i][upper_left_y]=1
        domain[upper_left_x+i][upper_left_y+(col_size-1)]=1
    for j in range(col_size):
        domain[upper_left_x,upper_left_y+j]=1
        domain[upper_left_x+(row_size-1),upper_left_y+j]=1
    return domain

def generate_Sigma_curve_on_domain(domain_sizes=25):
    domain=np.zeros((domain_sizes,domain_sizes),dtype=int)
    #define test domain size
    row_length=14
    vertical_length=15
    upper_left_x=3
    upper_left_y=3

    #make horizontal
    for j in range(row_length):
        domain[upper_left_x,upper_left_y+j]=1
        domain[upper_left_x+row_length,upper_left_y+j]=1
    for k in range(8):
        domain[upper_left_x+k][upper_left_y+k]=1
        domain[upper_left_x+vertical_length-1-k][upper_left_y+k]=1
    return domain
    

def collect_curve_coordinates(domain):
    coords=[]
    for ind,val in np.ndenumerate(domain):
        if val==1:
            coords.append(ind)
    return coords

def exist_start(domain,coords):
    for c in coords:
        sub_dom=[domain[tuple(c+np.array([i,j]))] for i in [-1,0,1] for j in [-1,0,1]]
        if np.count_nonzero(sub_dom)==2:
            return True,c
    return False,None

def condi(domain,traced,c,direc):
    if not np.all(direc==0) and domain[tuple(c+direc)]==1 and traced[tuple(c+direc)]==0:
        return True
    else:
        return False

def find_next_coord(dom,tr,c,direc):
    if dom[tuple(direc+c)]==1:
        return np.array(c+direc),direc
    else:
        candidates=[np.array([i,j]) for i in [-1,0,1] for j in [-1,0,1] if condi(dom,tr,c,np.array([i,j]))]
        dists=[abs(cand).sum() for cand in candidates]
        return np.array(candidates[np.argmin(dists)]+c),candidates[np.argmin(dists)]

if __name__ == '__main__':
    #domain=generate_square_on_domain()
    domain=generate_Sigma_curve_on_domain()
    print("create test domain\n",domain)
    coords=collect_curve_coordinates(domain)
    is_exist,start_coord=exist_start(domain,coords)
    if is_exist:
        print("start coordinate is",start_coord)
    else:
        print("this curve is link. We chose start coords from",coords[0])
        start_coord=coords[0]

    traced_table=np.zeros(domain.shape,dtype=int)
    traced_table[start_coord[0]][start_coord[1]]=1
    #set initial value
    #note that direc stands for direction
    coord=np.array(start_coord)
    direc=np.array([0,1])

    while(not np.all(domain==traced_table)):
        next_coord,next_direc=find_next_coord(domain,traced_table,coord,direc)
        #for debug
        print("next=",next_coord)
        print(next_direc)

        #update for next step
        coord=next_coord
        direc=next_direc
        traced_table[next_coord[0]][next_coord[1]]=1
        
        #for debug
        print(traced_table)

    print("finish !!!")
    print("track result=\n", traced_table)

