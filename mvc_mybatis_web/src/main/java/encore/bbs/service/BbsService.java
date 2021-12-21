package encore.bbs.service;

import java.util.List;

public interface BbsService {
	public List<Object> listService();
	public int postService(Object obj);
	public Object readService(Object obj);
	public int updateService(Object obj);
	public int deleteService(Object obj);
}
